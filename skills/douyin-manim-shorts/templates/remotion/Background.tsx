/* Background.tsx - Uniform tech background */
import React from "react";
import { AbsoluteFill, interpolate, useCurrentFrame } from "remotion";

interface BackgroundProps {
  bgmStyle?: string;
}

export const Background: React.FC<BackgroundProps> = ({ bgmStyle = "tech_fast" }) => {
  const frame = useCurrentFrame();

  const gradientAngle = interpolate(frame % 120, [0, 120], [0, 360]);
  const pulse = Math.sin(frame * 0.02) * 0.05 + 0.95;

  const gradientMap: Record<string, [string, string, string]> = {
    tech_fast: ["#09111f", "#142b2f", "#21183a"],
    deep_learning: ["#081826", "#1b263b", "#16251d"],
    math_gentle: ["#071b18", "#18212f", "#2a2438"],
    upbeat: ["#111827", "#2a2440", "#12343b"],
    calm: ["#0b1720", "#18251f", "#252033"],
  };

  const [color1, color2, color3] = gradientMap[bgmStyle] ?? gradientMap.tech_fast;

  return (
    <AbsoluteFill>
      <div
        style={{
          width: "100%",
          height: "100%",
          background: `linear-gradient(${gradientAngle}deg, ${color1}, ${color2}, ${color3})`,
          opacity: pulse,
        }}
      />
      {/* Subtle grid overlay */}
      <div
        style={{
          position: "absolute",
          top: 0,
          left: 0,
          width: "100%",
          height: "100%",
          backgroundImage:
            "linear-gradient(rgba(255,255,255,0.02) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.02) 1px, transparent 1px)",
          backgroundSize: "80px 80px",
          opacity: 0.3,
        }}
      />
    </AbsoluteFill>
  );
};
