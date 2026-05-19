/* TitleBlock.tsx - Title + hook reveal */
import React from "react";
import { interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { ZONES } from "./Layout";

interface TitleBlockProps {
  title: string;
  hook?: string[];
  enterFrame: number;
  exitFrame: number;
}

export const TitleBlock: React.FC<TitleBlockProps> = ({
  title,
  hook,
  enterFrame,
  exitFrame,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const opacity = interpolate(
    frame,
    [enterFrame, enterFrame + 5, exitFrame - 10, exitFrame],
    [0, 1, 1, 0],
    { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
  );

  const slideUp = spring({
    frame: frame - enterFrame,
    fps,
    config: { damping: 12, stiffness: 100 },
  });

  const zone = ZONES.titleArea;

  return (
    <div
      style={{
        position: "absolute",
        top: zone.top,
        left: 40,
        width: 1000,
        height: zone.height,
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
        alignItems: "center",
        opacity,
        transform: `translateY(${(1 - slideUp) * 30}px)`,
      }}
    >
      <h1
        style={{
          fontSize: 64,
          fontWeight: 800,
          color: "#ffffff",
          textAlign: "center",
          margin: 0,
          maxWidth: 960,
          overflow: "hidden",
          textOverflow: "ellipsis",
          whiteSpace: "nowrap",
        }}
      >
        {title}
      </h1>
      {hook?.map((line, i) => (
        <p
          key={i}
          style={{
            fontSize: 36,
            fontWeight: 500,
            color: i === 0 ? "#e0e0e0" : "#ffd700",
            textAlign: "center",
            margin: "4px 0",
            maxWidth: 900,
            overflow: "hidden",
            textOverflow: "ellipsis",
            whiteSpace: "nowrap",
          }}
        >
          {line}
        </p>
      ))}
    </div>
  );
};
