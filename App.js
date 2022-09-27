import {Route, Redirect, Switch, BrowserRouter as Router} from 'react-router-dom';

import Home from './pages/Home.js';
import Tracing from './pages/tracing.js';
import SingleStudent from './pages/singlestudent.js';
import Recommend from './pages/recommend.js';
import NotFoundPage from './pages/NotFoundPage.js';

function App() {
  return (
	<Router>
		<div>
			<Switch>
			{/* To be able to link to a new page, import the page as seen at the top, then copy the syntax from the Route below, replacing the data with your new data.*/}
			
				<Route exact path='/' component={Home} />
				<Route exact path='/tracing' component={Tracing} />
				<Route exact path='/singlestudent' component={SingleStudent}/>
				<Route exact path='/recommend' component={Recommend} />

				<Route exact path='/404' component={NotFoundPage} />
				<Redirect to='/404' />
			</Switch>
		</div>
	</Router>
  );
}

export default App;
