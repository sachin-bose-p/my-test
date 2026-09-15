import React from 'react';
import { Routes, Route } from 'react-router-dom';
import MainLayout from '../layouts/MainLayout';
import Counter from '../features/Counter';

const AppRoutes: React.FC = () => {
    return (
        <Routes>
            <Route path="/" element={<MainLayout />}>
                <Route index element={<Counter />} />
            </Route>
        </Routes>
    );

};

export default AppRoutes;