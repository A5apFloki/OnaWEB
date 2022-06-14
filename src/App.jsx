import * as React from "react";
import makeStyles from "@mui/styles/makeStyles";
import CustomDrawer from "./components/CustomDrawer";
import CustomMaps from "./components/Maps";
import CustomCard from "./components/CustomCard";
import NodeGraph from "./components/NodeGraph/nodeGraph";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";

const useStyles = makeStyles({
  root: {
    width: "100%",
    height: "100%",
  },
});

function App() {
  const classes = useStyles();

  return (
    <div className={classes.root}>
      <Router>
        <CustomDrawer />
        <Routes>
          <Route path="/dashboard" element={<CustomCard />} />
          <Route path="/oriented-graph" element={<NodeGraph />} />
          <Route path="/" element={<CustomMaps />} />
        </Routes>
      </Router>
    </div>
  );
}
export default App;
