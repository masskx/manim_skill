/* ManimClip.tsx - Embed Manim clip at position */
import React from "react";
import { OffthreadVideo, useCurrentFrame } from "remotion";
import { ZONES } from "./Layout";

interface ManimClipProps {
  src: string;
  startFrame: number;
  durationFrames: number;
}

export const ManimClip: React.FC<ManimClipProps> = ({
  src,
  startFrame,
  durationFrames,
}) => {
  const frame = useCurrentFrame();
  const zone = ZONES.visualArea;

  const localFrame = frame - startFrame;
  if (localFrame < 0 || localFrame >= durationFrames) {
    return null;
  }

  return (
    <div
      style={{
        position: "absolute",
        top: zone.top,
        left: 0,
        width: 1080,
        height: zone.height,
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        overflow: "hidden",
      }}
    >
      <OffthreadVideo
        src={src}
        style={{
          width: "100%",
          height: "100%",
          objectFit: "contain",
        }}
      />
    </div>
  );
};
