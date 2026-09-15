import React from 'react';

type DialogProps = {
  isOpen: boolean;
  onOk: () => void;
  onCancel: () => void;
};

const Dialog: React.FC<DialogProps> = ({ isOpen, onOk, onCancel, children }) => {
  if (!isOpen) return null;

  return (
    <div className="dialog">
      <div className="dialog-content">
        {children}
        <button onClick={onOk}>Ok</button>
        <button onClick={onCancel}>Cancel</button>
      </div>
    </div>
  );
};

export default Dialog;
