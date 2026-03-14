const tokenKeys = {
  access: "jwt_access",
  refresh: "jwt_refresh",
  pendingEmail: "jwt_pending_email",
};

const jsonHeaders = {
  "Content-Type": "application/json",
};

function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(";").shift();
  return "";
}

function getToken(type) {
  return localStorage.getItem(tokenKeys[type]);
}

function setToken(type, value) {
  if (value) {
    localStorage.setItem(tokenKeys[type], value);
  }
}

function clearTokens() {
  localStorage.removeItem(tokenKeys.access);
  localStorage.removeItem(tokenKeys.refresh);
}

function updateTokenIndicators() {
  document.querySelectorAll("[data-token]").forEach((el) => {
    const type = el.dataset.token;
    const value = getToken(type);
    el.textContent = value ? `${value.slice(0, 16)}...` : "Sem token";
  });
}

function extractMessage(payload, fallback) {
  if (!payload) return fallback;
  if (typeof payload === "string") return payload;
  if (payload.message) return payload.message;
  if (payload.error) return payload.error;
  if (payload.detail) return payload.detail;
  if (payload.valid === true) return "Token válido.";
  if (payload.valid === false) return "Token inválido.";
  if (payload["2fa_required"]) return "2FA necessário para continuar.";
  if (payload.access || payload.refresh) return "Operacao concluida.";
  const keys = Object.keys(payload);
  if (keys.length) {
    const firstKey = keys[0];
    if (firstKey === "access" || firstKey === "refresh") {
      return "Operacao concluida.";
    }
    const value = payload[firstKey];
    if (Array.isArray(value)) {
      return `${firstKey}: ${value[0]}`;
    }
    if (typeof value === "string") {
      return `${firstKey}: ${value}`;
    }
  }
  return fallback;
}

const errorMessages = {
  "/register/": "Nao foi possivel criar a conta. Verifique os dados informados.",
  "/login/": "Nao foi possivel autenticar. Verifique e-mail e senha.",
  "/logout/": "Nao foi possivel encerrar a sessao.",
  "/forgot_password/": "Nao foi possivel enviar o link. Verifique o e-mail.",
  "/reset_password/": "Nao foi possivel redefinir a senha. Verifique o link.",
  "/change_password/": "Nao foi possivel alterar a senha. Verifique os dados.",
  "/profile/": "Nao foi possivel carregar o perfil.",
  "/profile/update/": "Nao foi possivel atualizar o perfil.",
  "/token/verify/": "Nao foi possivel verificar o token.",
  "/token/refresh/": "Nao foi possivel renovar o token.",
  "/account/delete/": "Nao foi possivel excluir a conta.",
  "/2fa/verify/": "Nao foi possivel validar o 2FA.",
  "/2fa/enable/": "Nao foi possivel ativar o 2FA.",
  "/2fa/disable/": "Nao foi possivel desativar o 2FA.",
};

function getErrorFallback(endpoint) {
  if (!endpoint) return "Nao foi possivel concluir a operacao.";
  for (const key of Object.keys(errorMessages)) {
    if (endpoint.includes(key)) {
      return errorMessages[key];
    }
  }
  return "Nao foi possivel concluir a operacao.";
}

function showResult(container, payload, isError = false) {
  if (!container) return;
  container.classList.remove("success", "error");
  container.classList.add(isError ? "error" : "success");
  const fallback = isError ? "Nao foi possivel concluir a operacao." : "Operacao concluida.";
  container.textContent = extractMessage(payload, fallback);
}

function serializeForm(form) {
  const data = {};
  form.querySelectorAll("input, textarea, select").forEach((field) => {
    if (!field.name) return;
    if (field.type === "checkbox") {
      data[field.name] = field.checked;
      return;
    }
    if (field.value !== "") {
      data[field.name] = field.value;
    }
  });
  return data;
}

function buildEndpoint(form, payload) {
  const explicit = form.dataset.endpoint;
  const template = form.dataset.endpointTemplate;
  if (template) {
    const uid = payload.uid || "";
    const token = payload.token || "";
    if (!uid || !token) {
      return "";
    }
    const endpoint = template
      .replace("{uid}", encodeURIComponent(uid))
      .replace("{token}", encodeURIComponent(token));
    delete payload.uid;
    delete payload.token;
    return endpoint;
  }
  return explicit || "";
}

async function apiRequest({ endpoint, method, payload, useAuth }) {
  const headers = { ...jsonHeaders };
  const csrfToken = getCookie("csrftoken");
  if (csrfToken && method !== "GET") {
    headers["X-CSRFToken"] = csrfToken;
  }
  if (useAuth) {
    const access = getToken("access");
    if (access) {
      headers.Authorization = `Bearer ${access}`;
    }
  }

  const options = {
    method,
    headers,
    credentials: "same-origin",
  };

  if (method !== "GET") {
    options.body = JSON.stringify(payload || {});
  }

  const response = await fetch(endpoint, options);
  let data = null;
  try {
    data = await response.json();
  } catch (err) {
    data = { message: "" };
  }

  return { response, data };
}

function handleTokens(data) {
  if (data && data.access) {
    setToken("access", data.access);
  }
  if (data && data.refresh) {
    setToken("refresh", data.refresh);
  }
  updateTokenIndicators();
}

function setupForms() {
  document.querySelectorAll("form[data-endpoint]").forEach((form) => {
    form.addEventListener("submit", async (event) => {
      event.preventDefault();
      const result = form.parentElement.querySelector("[data-result]");
      const payload = serializeForm(form);

      if (form.dataset.useRefresh === "true") {
        const refresh = getToken("refresh");
        if (!refresh && !payload.refresh) {
          showResult(result, "Refresh token ausente no navegador.", true);
          return;
        }
        if (refresh && !payload.refresh) {
          payload.refresh = refresh;
        }
      }

      const endpoint = buildEndpoint(form, payload);
      if (!endpoint) {
        showResult(result, "Endpoint nao definido.", true);
        return;
      }

      const method = form.dataset.method || "POST";
      const useAuth = form.dataset.auth === "true";

      try {
        const { response, data } = await apiRequest({
          endpoint,
          method,
          payload,
          useAuth,
        });

        if (!response.ok) {
          const fallback = getErrorFallback(endpoint);
          const message = extractMessage(data, fallback);
          showResult(result, message, true);
          return;
        }

        if (data && data["2fa_required"]) {
          if (payload.email) {
            localStorage.setItem(tokenKeys.pendingEmail, payload.email);
          }
          showResult(result, data);
          window.location.assign("/app/2fa/verify/");
          return;
        }

        handleTokens(data);

        if (endpoint.includes("/logout/") || endpoint.includes("/account/delete/")) {
          clearTokens();
          updateTokenIndicators();
        }

        const redirect = form.dataset.redirect;
        if (redirect) {
          showResult(result, "Operacao concluida.");
          window.setTimeout(() => {
            window.location.assign(redirect);
          }, 150);
          return;
        }

        showResult(result, data);
      } catch (error) {
        const fallback = getErrorFallback(form.dataset.endpoint || "");
        showResult(result, fallback, true);
      }
    });
  });
}

function setupActions() {
  const clearBtn = document.querySelector("[data-action='clear-tokens']");
  if (clearBtn) {
    clearBtn.addEventListener("click", () => {
      clearTokens();
      updateTokenIndicators();
    });
  }

  const useAccessBtn = document.querySelector("[data-action='use-access']");
  if (useAccessBtn) {
    useAccessBtn.addEventListener("click", () => {
      const token = getToken("access");
      const textarea = document.querySelector("textarea[name='token']");
      if (token && textarea) {
        textarea.value = token;
      }
    });
  }

  const loadProfileBtn = document.querySelector("[data-action='load-profile']");
  if (loadProfileBtn) {
    loadProfileBtn.addEventListener("click", async () => {
      const result = document.querySelector("[data-result]");
      const nameEl = document.querySelector("[data-profile-name]");
      const emailEl = document.querySelector("[data-profile-email]");

      try {
        const { response, data } = await apiRequest({
          endpoint: "/profile/",
          method: "GET",
          payload: null,
          useAuth: true,
        });
        if (!response.ok) {
          const fallback = getErrorFallback("/profile/");
          const message = extractMessage(data, fallback);
          showResult(result, message, true);
          return;
        }
        if (nameEl) nameEl.textContent = data.name || "---";
        if (emailEl) emailEl.textContent = data.email || "---";
        showResult(result, "Perfil carregado.");
      } catch (error) {
        showResult(result, "Erro ao carregar perfil.", true);
      }
    });
  }
}

function setupPrefill() {
  document.querySelectorAll("[data-prefill='pending-email']").forEach((el) => {
    const value = localStorage.getItem(tokenKeys.pendingEmail);
    if (value) {
      el.value = value;
    }
  });
}

document.addEventListener("DOMContentLoaded", () => {
  updateTokenIndicators();
  setupForms();
  setupActions();
  setupPrefill();
});
