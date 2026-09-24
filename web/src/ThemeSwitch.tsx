import { useState } from "react";
import { Moon, Sun } from "lucide-react";
import { Button } from "@/components/ui/button";

const storageKey = "community-brain-theme";
type Theme = "light" | "dark";

export function initializeTheme(): Theme {
  let saved: string | null = null;
  try {
    saved = localStorage.getItem(storageKey);
  } catch {
    // Theme switching still works when browser storage is unavailable.
  }
  const theme =
    saved === "light" || saved === "dark"
      ? saved
      : window.matchMedia?.("(prefers-color-scheme: dark)").matches
        ? "dark"
        : "light";
  document.documentElement.dataset.theme = theme;
  return theme;
}

export function ThemeSwitch() {
  const [theme, setTheme] = useState(initializeTheme);
  function toggle() {
    const next = theme === "dark" ? "light" : "dark";
    document.documentElement.dataset.theme = next;
    setTheme(next);
    try {
      localStorage.setItem(storageKey, next);
    } catch {
      // Keep the selected appearance for this page even without storage.
    }
  }
  return (
    <Button
      variant="ghost"
      role="switch"
      aria-label="Dark mode"
      aria-checked={theme === "dark"}
      onClick={toggle}
      title={theme === "dark" ? "Switch to light mode" : "Switch to dark mode"}
    >
      {theme === "dark" ? <Moon /> : <Sun />}
      Dark mode
    </Button>
  );
}
