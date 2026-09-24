import React from "react";
import { createRoot } from "react-dom/client";
import {
  InMemoryWebStorage,
  UserManager,
  WebStorageStateStore,
} from "oidc-client-ts";
import { App } from "./App";
import { Api } from "./api";
import "./style.css";
import { initializeTheme, ThemeSwitch } from "./ThemeSwitch";

initializeTheme();

async function start() {
  const root = createRoot(document.getElementById("root")!);
  try {
    const response = await fetch("/auth-config.json");
    if (!response.ok)
      throw new Error("Sign-in has not been configured for this environment.");
    const config = await response.json();
    const manager = new UserManager({
      authority: config.authority,
      client_id: config.client_id,
      redirect_uri: location.origin + "/callback",
      post_logout_redirect_uri: location.origin,
      response_type: "code",
      scope: "openid profile",
      automaticSilentRenew: false,
      userStore: new WebStorageStateStore({ store: new InMemoryWebStorage() }),
    });
    const user =
      location.pathname === "/callback"
        ? await manager.signinRedirectCallback()
        : await manager.getUser();
    if (location.pathname === "/callback") history.replaceState({}, "", "/");
    if (!user || user.expired) {
      root.render(
        <main className="login">
          <div className="login-theme">
            <ThemeSwitch />
          </div>
          <h1>Community Brain</h1>
          <p>Your calls, ready to share.</p>
          <button onClick={() => void manager.signinRedirect()}>
            Sign in with Authentik
          </button>
        </main>,
      );
      return;
    }
    const api = new Api(async () => {
      if (user.expired) {
        await manager.signinRedirect();
        throw new Error("Sign in again");
      }
      return user.access_token;
    });
    root.render(
      <React.StrictMode>
        <App api={api} logout={() => void manager.signoutRedirect()} />
      </React.StrictMode>,
    );
  } catch (error) {
    root.render(
      <main className="login">
        <div className="login-theme">
          <ThemeSwitch />
        </div>
        <h1>Community Brain</h1>
        <p role="alert">
          {error instanceof Error ? error.message : "Unable to sign in."}
        </p>
      </main>,
    );
  }
}
void start();
