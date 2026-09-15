import React from 'react';

const AuthLayout: React.FC = ({ children }) => {
    return <div className="auth-layout">
        <header>
            <h1>Authentication</h1>
        </header>
        <main>{children}</main>
    </div>;
};

export default AuthLayout;