import React from 'react';

type DrawerProps = {
  isOpen: boolean;
  onClose: () => void;
};

const Drawer: React.FC<DrawerProps> = ({ isOpen, onClose, children }) => {
  return (
    <div className={`drawer ${isOpen ? 'open' : ''}`}>
      {children}
      <button onClick={onClose}>Close</button>
    </div>
  );
};

export default Drawer;
