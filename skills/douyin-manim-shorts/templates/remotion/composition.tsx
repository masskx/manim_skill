/* composition.tsx - Main composition that reads data.json and assembles all components */
import React from "react";
import { Sequence, useVideoConfig } from "remotion";
import { Layout } from "./components/Layout";
import { Background } from "./components/Background";
import { TitleBlock } from "./components/TitleBlock";
import { SubtitleBlock } from "./components/SubtitleBlock";
import { ManimClip } from "./components/ManimClip";
import { CodeCard } from "./components/CodeCard";
import { CTA } from "./components/CTA";
import data from "./data.json";

interface ClipConfig {
  type: string;
  path: string;
  start: number;
  duration: number;
}

interface CTAConfig {
  line1: string;
  line2: string;
}

interface SubtitleLine {
  start: number;
  end: number;
  text: string;
}

interface VideoData {
  moduleName: string;
  moduleType: string;
  title: string;
  hook: string[];
  clips: ClipConfig[];
  code: string[];
  highlightLine: number;
  cta: CTAConfig;
  bgmStyle: string;
  subtitleLines?: SubtitleLine[];
  totalDuration: number;
}

const videoData: VideoData = data as VideoData;

export const ModuleComposition: React.FC = () => {
  const { fps } = useVideoConfig();

  // Determine frame boundaries from data
  const hookEnd = videoData.clips.length > 0 ? videoData.clips[0].start * fps : fps * 6;
  const subtitleEnd = videoData.totalDuration ? videoData.totalDuration * fps - fps * 3 : fps * 23;

  return (
    <Layout>
      <Background bgmStyle={videoData.bgmStyle} />

      {/* Title + Hook: 0 to clip start */}
      <Sequence from={0} durationInFrames={hookEnd}>
        <TitleBlock
          title={videoData.title}
          hook={videoData.hook}
          enterFrame={0}
          exitFrame={hookEnd - 10}
        />
      </Sequence>

      {/* Manim clips */}
      {videoData.clips.map((clip, i) => {
        const startFrame = clip.start * fps;
        const durationFrames = clip.duration * fps;
        return (
          <Sequence key={i} from={startFrame} durationInFrames={durationFrames}>
            <ManimClip
              src={clip.path}
              startFrame={0}
              durationFrames={durationFrames}
            />
          </Sequence>
        );
      })}

      {/* Code Card: appears after last clip */}
      {(videoData.code?.length ?? 0) > 0 && (
        <Sequence
          from={
            videoData.clips.length > 0
              ? (videoData.clips[videoData.clips.length - 1].start +
                  videoData.clips[videoData.clips.length - 1].duration) *
                  fps +
                10
              : fps * 18
          }
          durationInFrames={fps * 5}
        >
          <CodeCard
            lines={videoData.code}
            highlightLine={videoData.highlightLine}
            enterFrame={0}
          />
        </Sequence>
      )}

      {/* Subtitles */}
      {(videoData.subtitleLines?.length ?? 0) > 0 && (
        <Sequence from={0} durationInFrames={Math.floor(videoData.totalDuration * fps)}>
          <SubtitleBlock lines={videoData.subtitleLines!} />
        </Sequence>
      )}

      {/* CTA: last 3 seconds */}
      <Sequence from={subtitleEnd} durationInFrames={fps * 3}>
        <CTA
          line1={videoData.cta.line1}
          line2={videoData.cta.line2}
          enterFrame={0}
        />
      </Sequence>
    </Layout>
  );
};
