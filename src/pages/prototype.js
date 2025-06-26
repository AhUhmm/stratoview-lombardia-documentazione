import React, { useState, useEffect } from "react";
import Layout from "@theme/Layout";
import styles from "./prototype.module.css";

export default function Prototype() {
  const [isFullscreen, setIsFullscreen] = useState(false);
  const [viewMode, setViewMode] = useState("embedded"); // embedded, expanded, fullscreen

  useEffect(() => {
    const handleFullscreenChange = () => {
      setIsFullscreen(!!document.fullscreenElement);
    };

    document.addEventListener("fullscreenchange", handleFullscreenChange);
    return () =>
      document.removeEventListener("fullscreenchange", handleFullscreenChange);
  }, []);

  const toggleFullscreen = () => {
    const iframe = document.getElementById("prototypeFrame");
    if (!document.fullscreenElement) {
      iframe.requestFullscreen();
    } else {
      document.exitFullscreen();
    }
  };

  return (
    <Layout
      title="Interactive Prototype"
      description="Stratoview Interactive Prototype"
      noFooter={viewMode === "expanded"}
    >
      <div className={styles.container}>
        <div className={styles.controls}>
          <div className={styles.controlGroup}>
            <button
              onClick={() => setViewMode("embedded")}
              className={`${styles.controlBtn} ${
                viewMode === "embedded" ? styles.active : ""
              }`}
            >
              📱 Embedded
            </button>
            <button
              onClick={() => setViewMode("expanded")}
              className={`${styles.controlBtn} ${
                viewMode === "expanded" ? styles.active : ""
              }`}
            >
              📐 Expanded
            </button>
            <button onClick={toggleFullscreen} className={styles.controlBtn}>
              {isFullscreen ? "🗙 Exit Fullscreen" : "⛶ Fullscreen"}
            </button>
          </div>
          <a
            href="/mockup/interactive-prototype.html"
            target="_blank"
            className={styles.newTabBtn}
          >
            ↗ New Tab
          </a>
        </div>

        <div className={styles[viewMode]}>
          <iframe
            id="prototypeFrame"
            src="/mockup/interactive-prototype.html"
            className={styles.iframe}
            title="Stratoview Interactive Prototype"
          />
        </div>
      </div>
    </Layout>
  );
}
