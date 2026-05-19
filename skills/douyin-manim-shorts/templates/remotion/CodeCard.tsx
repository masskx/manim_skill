/* CodeCard.tsx - Code card with highlight */
import React from "react";
import { interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { ZONES } from "./Layout";

interface CodeCardProps {
  lines: string[];
  highlightLine: number;
  enterFrame: number;
  maxLines?: number;
}

const CODE_FONT = '"JetBrains Mono", "Fira Code", "Consolas", monospace';

export const CodeCard: React.FC<CodeCardProps> = ({
  lines,
  highlightLine,
  enterFrame,
  maxLines = 6,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const displayLines = lines.slice(0, maxLines);

  const progress = spring({
    frame: Math.max(0, frame - enterFrame),
    fps,
    config: { damping: 14, stiffness: 80 },
  });

  const opacity = interpolate(
    frame,
    [enterFrame - 5, enterFrame, enterFrame + fps * 0.3],
    [0, 0, 1],
    { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
  );

  const zone = ZONES.infoArea;

  return (
    <div
      style={{
        position: "absolute",
        top: zone.top + 10,
        left: 60,
        width: 960,
        height: zone.height - 20,
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        opacity,
      }}
    >
      <div
        style={{
          backgroundColor: "#1a1a2e",
          borderRadius: 16,
          padding: "24px 32px",
          width: "100%",
          maxWidth: 920,
          transform: `scale(${0.9 + progress * 0.1})`,
          border: "1px solid #2a2a4a",
        }}
      >
        <div
          style={{
            display: "flex",
            flexDirection: "column",
            gap: 8,
          }}
        >
          {displayLines.map((line, i) => {
            const isHighlighted = i + 1 === highlightLine;
            return (
              <div
                key={i}
                style={{
                  display: "flex",
                  alignItems: "center",
                  gap: 16,
                  backgroundColor: isHighlighted
                    ? "rgba(255, 215, 0, 0.12)"
                    : "transparent",
                  borderRadius: 8,
                  padding: "4px 12px",
                  borderLeft: isHighlighted ? "4px solid #ffd700" : "4px solid transparent",
                }}
              >
                <span
                  style={{
                    fontSize: 18,
                    color: "#666",
                    minWidth: 28,
                    textAlign: "right",
                    fontFamily: CODE_FONT,
                  }}
                >
                  {i + 1}
                </span>
                <code
                  style={{
                    fontSize: 28,
                    fontFamily: CODE_FONT,
                    color: isHighlighted ? "#ffd700" : "#e0e0e0",
                    fontWeight: isHighlighted ? 700 : 400,
                    whiteSpace: "pre",
                    overflow: "hidden",
                    textOverflow: "ellipsis",
                    maxWidth: 800,
                  }}
                >
                  {line}
                </code>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
};
