/* Layout.tsx - Global 9:16 safe-area container */
import React from "react";
import { AbsoluteFill } from "remotion";

const TITLE_AREA_TOP = 80;
const TITLE_AREA_BOTTOM = 260;
const VISUAL_AREA_TOP = 300;
const VISUAL_AREA_BOTTOM = 1180;
const INFO_AREA_TOP = 1200;
const INFO_AREA_BOTTOM = 1500;
const SUBTITLE_AREA_TOP = 1540;
const SUBTITLE_AREA_BOTTOM = 1660;
const CTA_AREA_TOP = 1680;
const CTA_AREA_BOTTOM = 1820;

interface LayoutProps {
  children: React.ReactNode;
  background?: string;
}

export const Layout: React.FC<LayoutProps> = ({
  children,
  background = "#0a0a1a",
}) => {
  return (
    <AbsoluteFill
      style={{
        backgroundColor: background,
        width: 1080,
        height: 1920,
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        overflow: "hidden",
        fontFamily: '"Noto Sans SC", "Microsoft YaHei", sans-serif',
      }}
    >
      {children}
    </AbsoluteFill>
  );
};

export const ZONES = {
  titleArea: {
    top: TITLE_AREA_TOP,
    bottom: TITLE_AREA_BOTTOM,
    height: TITLE_AREA_BOTTOM - TITLE_AREA_TOP,
  },
  visualArea: {
    top: VISUAL_AREA_TOP,
    bottom: VISUAL_AREA_BOTTOM,
    height: VISUAL_AREA_BOTTOM - VISUAL_AREA_TOP,
  },
  infoArea: {
    top: INFO_AREA_TOP,
    bottom: INFO_AREA_BOTTOM,
    height: INFO_AREA_BOTTOM - INFO_AREA_TOP,
  },
  subtitleArea: {
    top: SUBTITLE_AREA_TOP,
    bottom: SUBTITLE_AREA_BOTTOM,
    height: SUBTITLE_AREA_BOTTOM - SUBTITLE_AREA_TOP,
  },
  ctaArea: {
    top: CTA_AREA_TOP,
    bottom: CTA_AREA_BOTTOM,
    height: CTA_AREA_BOTTOM - CTA_AREA_TOP,
  },
};
