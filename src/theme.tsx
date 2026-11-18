import type { CSSProperties, ReactNode } from "react";

/** Tema claro e colorido, equivalente ao useGrokTheme do canvas (marca Grok / Sand). */
export function useGrokTheme() {
  return {
    font: {
      family: '"Nunito", "Segoe UI", "Helvetica Neue", Arial, sans-serif',
    },
    bg: {
      base: "#F6F3EE",
      elevated: "#FFFFFF",
    },
    border: {
      subtle: "#E6E0D4",
      default: "#D4CDBF",
    },
    text: {
      primary: "#1A1714",
      secondary: "#5C564C",
      tertiary: "#8A8378",
      accent: "#0B63D6",
      onColor: "#FFFFFF",
      danger: "#C0172F",
      warning: "#B15C00",
      success: "#0A7A3E",
    },
    fill: {
      dangerSubtle: "#FDE8EA",
      warningSubtle: "#FFF3D6",
      successSubtle: "#E3F6EA",
      accentSubtle: "#E8F2FF",
    },
    dataviz: {
      // Cores sólidas (sem alfa) para bordas e fundos de cards
      categorical: [
        "#1084FE",
        "#FF6700",
        "#7B3FF2",
        "#00A85A",
        "#E31C79",
        "#0D9488",
        "#E59B0B",
      ],
    },
  };
}

export function Image({
  src,
  alt,
  fit,
  width,
  height,
}: {
  src: string;
  alt: string;
  fit?: string;
  width?: number;
  height?: number;
}) {
  const url = src.startsWith("asset:") ? `fotos/${src.slice(6)}` : src;
  const style: CSSProperties = {
    width: width ?? "100%",
    height: height ?? "100%",
    objectFit: (fit as CSSProperties["objectFit"]) || "cover",
    display: "block",
  };
  return <img src={url} alt={alt} style={style} />;
}

export function Page({
  children,
}: {
  title?: string;
  width?: string;
  children?: ReactNode;
}) {
  return <>{children}</>;
}
