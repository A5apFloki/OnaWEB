import * as React from "react";
import SwipeableDrawer from "@mui/material/SwipeableDrawer";
import IconButton from "@mui/material/IconButton";
import { NavLink } from "react-router-dom";
import List from "@mui/material/List";
import ListItem from "@mui/material/ListItem";
import ListItemIcon from "@mui/material/ListItemIcon";
import ListItemText from "@mui/material/ListItemText";
import ArrowForward from "@mui/icons-material/ArrowForward";
import ArrowBack from "@mui/icons-material/ArrowBack";
import MapIcon from "@mui/icons-material/Map";
import HubIcon from "@mui/icons-material/Hub";
import DashboardIcon from "@mui/icons-material/Dashboard";
import PDFIcon from "@mui/icons-material/PictureAsPdf";
import makeStyles from "@mui/styles/makeStyles";
import clsx from "clsx";

const useStyles = makeStyles({
  drawerContainer: {
    width: 250,
    paddingTop: 28,
    "& .MuiButtonBase-root": {
      paddingLeft: 40,
    },
  },
  openDrawerButton: {
    position: "absolute !important",
    zIndex: 1201,
    top: 5,
    left: 5,
    "&.MuiButtonBase-root": {
      backgroundColor: ({ drawerOpen }) => {
        return !drawerOpen ? "rgb(25 118 210 / 80%)" : "transparent";
      },
      color: ({ drawerOpen }) => (!drawerOpen ? "#fff" : "#1976d2"),
      "&:hover": {
        backgroundColor: ({ drawerOpen }) => {
          return !drawerOpen
            ? "rgb(25 118 210 / 70%)"
            : "rgba(25, 118, 210, 0.04)";
        },
      },
    },
  },
  link: {
    textDecoration: "none !important",
    color: "#000 !important",
    "&:hover": {
      "& .MuiSvgIcon-root": {
        color: "#000 !important",
      },
      "& > .MuiButtonBase-root:hover": {
        color: "#000 !important",
        backgroundColor: "#1976d2c2 !important",
      },
    },
  },
  activeLink: {
    color: "#fff !important",
    "& .MuiSvgIcon-root": {
      color: "#fff",
    },
    "& > .MuiButtonBase-root": {
      backgroundColor: "#1976d2",
    },
  },
});

const listItems = [
  { text: "Map", path: "/", Icon: <MapIcon /> },
  { text: "Graphe (Orienté)", path: "oriented-graph", Icon: <HubIcon /> },
  { text: "Tableau de Bord", path: "dashboard", Icon: <DashboardIcon /> },
  { text: "Rapports", path: "repports", Icon: <PDFIcon /> },
];

function CustomDrawer() {
  const [drawerOpen, setDrawerOpen] = React.useState(false);
  const classes = useStyles({ drawerOpen });

  const handleOpenDrawer = (e, isOpen) => {
    setDrawerOpen(isOpen !== undefined ? isOpen : !drawerOpen);
  };

  return (
    <>
      <IconButton
        color="primary"
        aria-label="upload picture"
        component="span"
        className={classes.openDrawerButton}
        onClick={handleOpenDrawer}
      >
        {!drawerOpen ? <ArrowForward /> : <ArrowBack />}
      </IconButton>
      <SwipeableDrawer
        anchor="left"
        open={drawerOpen}
        onClose={(e) => handleOpenDrawer(e, false)}
        onOpen={(e) => handleOpenDrawer(e, true)}
      >
        <div
          className={classes.drawerContainer}
          onClick={(e) => handleOpenDrawer(e, false)}
        >
          <List>
            {listItems.map((item) => (
              <NavLink
                className={({ isActive }) =>
                  !isActive
                    ? classes.link
                    : clsx(classes.link, classes.activeLink)
                }
                to={item.path}
                key={`${item.text}-${item.path}`}
              >
                <ListItem button>
                  <ListItemIcon>{item.Icon}</ListItemIcon>
                  <ListItemText primary={item.text} />
                </ListItem>
              </NavLink>
            ))}
          </List>
          {/* <Divider /> */}
        </div>
      </SwipeableDrawer>
    </>
  );
}

export default CustomDrawer;
