import React, { Component } from 'react';
import Link from '@material-ui/core/Link';
import logo from '../../build_you_logo.png';

import { login_request } from '../../actions/auth/login';

export default class Home extends Component {
    componentDidMount() {
        console.log(login_request('test','test'));
    }

    render() {
        return (
            <div className='App'>
                <header className='App-header'>
                    <img src={logo} className="App-logo" alt="logo" />
                    <Link href={'/login'}>Вхід</Link>
                </header>
            </div>
        )
    }
}