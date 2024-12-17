import React, { Component } from 'react';
import { LineChart, Line, AreaChart, Area, CartesianGrid, XAxis, YAxis, Tooltip } from 'recharts';

export class Graph extends Component {

  render() {

    const data = this.props.data;
    console.log(data)
    return (
      <div className="profileview mb-3">Stock Price
        <LineChart width={1100} height={300} data={data} >
          <Line type="monotone" dataKey="val" stroke="#8884d8"/>
          {/*<Line type="monotone" dataKey="low" stroke="#000"/>*/}
          <CartesianGrid stroke="#ccc" />
          <XAxis dataKey="day"  />
          <YAxis dataKey="val"  />
          {/*<YAxis dataKey="low"  />*/}
          <Tooltip />
        </LineChart>
        <span style={{float:"right"}}>Last 5 Days</span>
      </div>
    )
  }
}

export default Graph
