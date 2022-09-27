import React, { Component } from "react";
import ReactDOM from "react-dom";
import Graph from "react-graph-vis";
import { BrowserRouter, Route, Switch } from 'react-router-dom'
import ButtonAppBar from './buttonAppBar.js';

class Recommend extends Component {  
	constructor() {
    super();
    this.state = {
      options: {
        layout: {
          // hierarchical: true,
        },
        edges: {
          color: "#000000"
        },
        nodes: {
          color: "#888f99"
        },
        physics: {
          enabled: true
        },
        interaction: { multiselect: true, dragView: true }
      },
      graph: {
        nodes: [
          { id: 1, label: "Node 1" },
          { id: 2, label: "Node 2" },
          { id: 3, label: "Node 3" },
          { id: 4, label: "Node 4" },
          { id: 5, label: "Node 5" }
        ],
        edges: [
          { from: 1, to: 2 },
          { from: 1, to: 3 },
          { from: 2, to: 4 },
          { from: 2, to: 5 }
        ]
      }
    };
  }

  componentDidMount() {
    document.addEventListener("mousedown", e => {});
    document.addEventListener("mousemove", e => {});
  }

  events = {
    dragStart: event => {},
    dragEnd: event => {}
  };

  render() {
    return (
      <div id="graph" style={{ height: "100vh" }}>
		<div>
		<ButtonAppBar heading={`Recommended Actions`}/>
		</div>
        <Graph
          graph={this.state.graph}
          options={this.state.options}
          events={this.state.events}
        />
      </div>
    );
  }
}

export default Recommend;