import React, { useState } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';
import IconButton from '@material-ui/core/IconButton';
import MenuIcon from '@material-ui/icons/Menu';
import { Drawer } from '@material-ui/core';
import ChevronLeftIcon from '@material-ui/icons/ChevronLeft';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemText from '@material-ui/core/ListItemText';
import { Link } from "react-router-dom";

{/* Style data. Determines how the app bar appears.*/}

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
  },
  menuButton: {
    marginRight: theme.spacing(2),
  },
  title: {
    flexGrow: 1,
  },
}));

export default function ButtonAppBar(props) {
  const [drawerIsOpen, setDrawerIsOpen] = useState(false);
  const classes = useStyles();

  return (
    <div className={classes.root}>
      <AppBar position="static">
        <Toolbar>
          <IconButton onClick={() => setDrawerIsOpen(true)} edge="start" className={classes.menuButton} color="inherit" aria-label="menu">
            <MenuIcon />
          </IconButton>
          <Typography variant="h6" className={classes.title}>
            {props.heading}
          </Typography>
        </Toolbar>
      </AppBar>
      <Drawer
          variant="temporary"
          classes={{
            paper: classes.drawerPaper,
          }}
          open={drawerIsOpen}>
          <div className={classes.drawerHeader}>
            <IconButton onClick={() => setDrawerIsOpen(false)}>
              <ChevronLeftIcon />
            </IconButton>
          </div>
          <List>
          
          {/* To add an item to the menu of the AppBar, copy the ListItem syntax as shown below, then link it.
              To link a new page, route it in /src/App.js then the link will work here.*/}
          
            <ListItem button component={Link} to="/">
              <ListItemText>Home</ListItemText>
            </ListItem>
            <ListItem button component={Link} to="/tracing">
              <ListItemText>Trace Graph</ListItemText>
            </ListItem>
            <ListItem button component={Link} to="/singlestudent">
              <ListItemText>Single Student View</ListItemText>
            </ListItem>
            <ListItem button component={Link} to="/recommend">
              <ListItemText>Recommended Actions</ListItemText>
            </ListItem>

          </List>
        </Drawer>
    </div>
  );
}