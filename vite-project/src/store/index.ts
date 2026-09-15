import { configureStore } from '@reduxjs/toolkit';
import { createSlice } from '@reduxjs/toolkit';
import { Provider } from 'react-redux';

// AppProvider component to wrap the application with Redux
// Add any additional reducers or middleware here if needed in the future.
// For now, only a simple counterSlice has been included for demonstration.
export const AppProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => (
  <Provider store={store}>
    {children}
  </Provider>
);


// Example slice for demonstration purposes
const counterSlice = createSlice({
  name: 'counter',
  initialState: 0,
  reducers: {
    increment: state => state + 1,
    decrement: state => state - 1,
  },
});


const store = configureStore({
  reducer: {
    counter: counterSlice.reducer,
  },
});


const store = configureStore({
  reducer: {
    counter: counterSlice.reducer,
  },
});

export default store;
