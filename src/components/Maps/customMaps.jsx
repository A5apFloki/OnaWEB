import GoogleMapReact from "google-map-react";
import makeStyles from "@mui/styles/makeStyles";
import Person from "@mui/icons-material/Person";

const Marker = () => (
  <div>
    <Person />
  </div>
);

const useStyles = makeStyles({
  mapContainer: {
    position: "absolute",
    top: 0,
    left: 0,
    zIndex: 1,
    width: "100%",
    height: "100vh",
  },
});

const defaultProps = {
  center: {
    lat: 36.820344103027615,
    lng: 7.714581370296837,
  },
  zoom: 15,
};

const CustomMaps = () => {
  const classes = useStyles();

  const handleApiLoaded = (map, maps) => {};

  return (
    <div className={classes.mapContainer}>
      <GoogleMapReact
        bootstrapURLKeys={{ key: "AIzaSyBHlbIHEr1Jfo_99EIfi870YUHRUfc2QKE" }}
        defaultCenter={defaultProps.center}
        defaultZoom={defaultProps.zoom}
        onGoogleApiLoaded={({ map, maps }) => handleApiLoaded(map, maps)}
        options={(maps) => ({
          fullscreenControl: false,
          // mapTypeId: maps.MapTypeId.SATELLITE,
        })}
        yesIWantToUseGoogleMapApiInternals
      >
        <Marker lat={36.820281644101755} lng={7.715169516991862} />
        <Marker lat={36.82024943669526} lng={7.7150394298562714} />
      </GoogleMapReact>
    </div>
  );
};

export default CustomMaps;
