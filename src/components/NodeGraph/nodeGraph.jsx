import React from "react";
import ForceGraph2D from "react-force-graph-2d";
import drain from "../../assets/icons/drain.png";

const drainImage = new Image();
drainImage.src = drain;

const genRandomTree = (N = 300, reverse = false) => {
  return {
    nodes: [...Array(N).keys()].map((i) => ({ id: i })),
    links: [...Array(N).keys()]
      .filter((id) => id)
      .map((id) => ({
        [reverse ? "target" : "source"]: id,
        [reverse ? "source" : "target"]: Math.round(Math.random() * (id - 1)),
      })),
  };
};

const drawNodes = ({ x, y }, ctx) => {
  const size = 15;
  ctx.drawImage(drainImage, x - size / 2, y - size / 2, size, size);
};

const linkColor = () => "rgba(0, 0, 0, 0.5)";

function NodeGraph() {
  const fd2dRef = React.useRef(null);

  React.useEffect(() => {
    if (fd2dRef && fd2dRef.current) {
      const { current: ctx } = fd2dRef;
      ctx.zoom(2);
    }
  }, []);

  return (
    // <div style={{ overflow: "hidden" }}>
    <ForceGraph2D
      ref={fd2dRef}
      // width={1920}
      // height={1080}
      graphData={genRandomTree(20)}
      nodeLabel="id"
      linkWidth={2}
      linkColor={linkColor}
      nodeCanvasObject={drawNodes}
      //   cooldownTicks={100}
      //   onEngineStop={() => fd2dRef.current.zoomToFit(500)}
    />
    // </div>
  );
}

export default NodeGraph;
