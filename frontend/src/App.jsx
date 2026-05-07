import { useEffect, useRef, useState } from "react";
import Webcam from "react-webcam";

function App() {
  const webcamRef = useRef(null);

  const wsRef = useRef(null);

  const [processedFrame, setProcessedFrame] = useState(null);

  useEffect(() => {
    wsRef.current = new WebSocket("ws://127.0.0.1:8000/ws/video");

    wsRef.current.onmessage = async (event) => {
      const blob = event.data;

      const imageUrl = URL.createObjectURL(blob);

      setProcessedFrame(imageUrl);
    };

    const interval = setInterval(() => {
      captureFrame();
    }, 500);

    return () => clearInterval(interval);
  }, []);

  const captureFrame = async () => {
    if (!webcamRef.current) return;

    const screenshot = webcamRef.current.getScreenshot();

    if (!screenshot) return;

    const blob = await fetch(screenshot).then((res) => res.blob());

    if (wsRef.current.readyState === WebSocket.OPEN) {
      wsRef.current.send(blob);
    }
  };

  return (
    <div
      style={{
        minHeight: "100vh",
        backgroundColor: "#0f172a",
        color: "white",
        padding: "32px",
        fontFamily: "Arial",
      }}
    >
      <h1
        style={{
          textAlign: "center",
          marginBottom: "40px",
          fontSize: "2rem",
        }}
      >
        Real-Time Face Detection System
      </h1>

      <div
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(auto-fit, minmax(320px, 1fr))",
          gap: "24px",
        }}
      >
        <div
          style={{
            background: "#1e293b",
            padding: "20px",
            borderRadius: "16px",
            boxShadow: "0 4px 20px rgba(0,0,0,0.3)",
          }}
        >
          <h2
            style={{
              marginBottom: "16px",
              textAlign: "center",
            }}
          >
            Original Feed
          </h2>

          <Webcam
            ref={webcamRef}
            screenshotFormat="image/jpeg"
            style={{
              width: "100%",
              borderRadius: "12px",
            }}
          />
        </div>

        <div
          style={{
            background: "#1e293b",
            padding: "20px",
            borderRadius: "16px",
            boxShadow: "0 4px 20px rgba(0,0,0,0.3)",
          }}
        >
          <h2
            style={{
              marginBottom: "16px",
              textAlign: "center",
            }}
          >
            Processed Feed
          </h2>

          {processedFrame ? (
            <img
              src={processedFrame}
              alt="Processed"
              style={{
                width: "100%",
                borderRadius: "12px",
              }}
            />
          ) : (
            <div
              style={{
                height: "240px",
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
                color: "#94a3b8",
              }}
            >
              Waiting for processed frames...
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default App;
