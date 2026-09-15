import { configureStore } from '@reduxjs/toolkit';

const store = configureStore({
  reducer: {
    // Add your slices here
    // Example: user: userSlice,
    // Add future slices for features
  },
});

export default store;
