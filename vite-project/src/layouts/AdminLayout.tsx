import React from 'react';

const AdminLayout: React.FC = ({ children }) => {
    return <div className="admin-layout">
        <header>Admin Panel</header>
        <main>{children}</main>
    </div>;
};

export default AdminLayout;