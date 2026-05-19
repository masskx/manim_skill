/* CTA.tsx - Resource pack CTA */
import React from "react";
import { interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { ZONES } from "./Layout";

interface CTAProps {
  line1: string;
  line2: string;
  enterFrame: number;
}

export const CTA: React.FC<CTAProps> = ({ line1, line2, enterFrame }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const progress = spring({
    frame: Math.max(0, frame - enterFrame),
    fps,
    config: { damping: 12, stiffness: 90 },
  });

  const opacity = interpolate(
    frame,
    [enterFrame, enterFrame + 8],
    [0, 1],
    { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
  );

  const zone = ZONES.ctaArea;

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
        transform: `translateY(${(1 - progress) * 40}px)`,
      }}
    >
      <div
        style={{
          backgroundColor: "rgba(255, 215, 0, 0.1)",
          border: "2px solid #ffd700",
          borderRadius: 16,
          padding: "20px 40px",
          textAlign: "center",
          maxWidth: 920,
        }}
      >
        <p
          style={{
            fontSize: 34,
            fontWeight: 700,
            color: "#ffd700",
            margin: "0 0 8px 0",
            maxWidth: 840,
            overflow: "hidden",
            textOverflow: "ellipsis",
            whiteSpace: "nowrap",
          }}
        >
          {line1}
        </p>
        <p
          style={{
            fontSize: 28,
            fontWeight: 500,
            color: "#ffffff",
            margin: 0,
            maxWidth: 840,
            overflow: "hidden",
            textOverflow: "ellipsis",
            whiteSpace: "nowrap",
          }}
        >
          {line2}
        </p>
      </div>
    </div>
  );
};
