import React, { Component } from 'react';

import {
    Route,
    Switch,
    withRouter
} from 'react-router-dom';

import Home from './components/Home/Home';
import SignIn from './components/SignIn/SignIn';
import SignUp from './components/SignUp/SignUp';

import './index.css';
import './App.css';

class App extends Component {
    render() {
        const { history } = this.props

        return (
            <div className='App'>
                <Switch>
                    <Route exact history={history} path='/login' component={SignIn} />
                    <Route exact history={history} path='/register' component={SignUp} />
                    <Route history={history} path='/' component={Home} />
                </Switch>
            </div>
        );
    }
}

export default withRouter(App)