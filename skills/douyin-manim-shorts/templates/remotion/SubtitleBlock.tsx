/* SubtitleBlock.tsx - Timed subtitle rendering */
import React from "react";
import { useCurrentFrame, useVideoConfig } from "remotion";
import { ZONES } from "./Layout";

interface SubtitleLine {
  start: number;
  end: number;
  text: string;
}

interface SubtitleBlockProps {
  lines: SubtitleLine[];
}

export const SubtitleBlock: React.FC<SubtitleBlockProps> = ({ lines }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const currentTime = frame / fps;
  const activeLine = lines.find(
    (l) => currentTime >= l.start && currentTime <= l.end
  );

  const zone = ZONES.subtitleArea;

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
      }}
    >
      {activeLine && (
        <div
          style={{
            backgroundColor: "rgba(0, 0, 0, 0.7)",
            borderRadius: 12,
            padding: "12px 32px",
            maxWidth: 900,
          }}
        >
          <p
            style={{
              fontSize: 38,
              fontWeight: 600,
              color: "#ffffff",
              textAlign: "center",
              margin: 0,
              maxWidth: 840,
              overflow: "hidden",
              textOverflow: "ellipsis",
              lineHeight: 1.4,
            }}
          >
            {activeLine.text}
          </p>
        </div>
      )}
    </div>
  );
};
