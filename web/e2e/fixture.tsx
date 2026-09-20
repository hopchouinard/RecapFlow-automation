// Browser-test entrypoint only; not imported by the production application.
import { createRoot } from "react-dom/client";
import { App } from "../src/App";
import { Api } from "../src/api";
import "../src/style.css";
createRoot(document.getElementById("root")!).render(
  <App api={new Api(async () => "fixture")} logout={() => {}} />,
);
