import { useState, type ReactNode } from "react";
import Markdown from "react-markdown";
import remarkGfm from "remark-gfm";
import { Button } from "@/components/ui/button";

export function FilePreview({
  name,
  text,
  children,
}: {
  name: string;
  text: string;
  children: ReactNode;
}) {
  const [rendered, setRendered] = useState(false);
  const markdown = /\.(md|markdown)(\.legacy)?$/i.test(name);
  return (
    <div className="preview">
      <div className="panel-heading">
        <strong>{name}</strong>
        <div className="actions">
          {markdown && (
            <div
              className="preview-toggle"
              role="group"
              aria-label="Markdown view"
            >
              <Button
                size="sm"
                variant={rendered ? "ghost" : "secondary"}
                aria-pressed={!rendered}
                onClick={() => setRendered(false)}
              >
                Raw
              </Button>
              <Button
                size="sm"
                variant={rendered ? "secondary" : "ghost"}
                aria-pressed={rendered}
                onClick={() => setRendered(true)}
              >
                Rendered
              </Button>
            </div>
          )}
          {children}
        </div>
      </div>
      {markdown && rendered ? (
        <div className="markdown-content" aria-label="Rendered Markdown">
          <Markdown
            remarkPlugins={[remarkGfm]}
            skipHtml
            components={{
              a: ({ children, href }) => (
                <a
                  href={href}
                  target={href?.startsWith("#") ? undefined : "_blank"}
                  rel="noopener noreferrer"
                >
                  {children}
                </a>
              ),
              img: ({ alt }) => (
                <span className="muted">[Image{alt ? `: ${alt}` : ""}]</span>
              ),
            }}
          >
            {text}
          </Markdown>
        </div>
      ) : (
        <pre aria-label="Raw file contents">{text}</pre>
      )}
    </div>
  );
}
