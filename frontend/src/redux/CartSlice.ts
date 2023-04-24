import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";

export const fetchCartData = createAsyncThunk("fetchCartData", async () => {
  const response = await fetch("http://127.0.0.1:8000/cart/");
  return response.json();
});

export const CartSlice = createSlice({
  name: "cart",
  initialState: {
    Url: "http://127.0.0.1:8000",
    loading: false,
    cartData: [],
    error: true,
    countValue:0,
  },
  reducers: {
    increaseCounter: (state, action) => {
      state.countValue = action.payload;
    },
  },
  extraReducers: (builder) => {
    builder.addCase(fetchCartData.pending, (state) => {
      state.loading = true;
    });
    builder.addCase(fetchCartData.fulfilled, (state, action) => {
      state.loading = false;
      state.cartData = action.payload;
    });
    builder.addCase(fetchCartData.rejected, (state) => {
      state.error = true;
    });
  },
});

export const { increaseCounter } = CartSlice.actions;

export default CartSlice.reducer;
