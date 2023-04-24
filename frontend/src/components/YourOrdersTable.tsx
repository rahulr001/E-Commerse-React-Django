import * as React from "react";
import Box from "@mui/material/Box";
import { DataGrid, GridColDef } from "@mui/x-data-grid";
import QuantityBtn from "../utils/QuantityBtn";
import { DeleteOutlined } from "@ant-design/icons";
import { IconButton } from "@mui/material";
import { useSelector, useDispatch } from "react-redux";
import { fetchCartData } from "../redux/CartSlice";
import axios from "axios";

export default function YourOrdersTable({ cart }) {
  const dispatch = useDispatch();
  const url = useSelector((state) => state.CartSlice.Url);
  const counterValue = useSelector(
    (state) => state.CartSlice.countValue.countValue
  );
  const [rowId, setRowId] = React.useState(0);
  const handleDelete = async (params) => {
    if (window.confirm("Are you sure you want to delete the item")) {
      await axios
        .delete(`${url}/cart/${params.id}/delete`)
        .then(() => dispatch(fetchCartData()));
    }
  };

  const cartItems = cart.filter((items) => items.PaymentStatus === false);
  const columns: GridColDef[] = [
    {
      field: "ImageURL",
      headerName: "",
      type: "image",
      width: 250,
      renderCell: (params) => {
        return (
          <img
            style={{ height: 130, width: 130 }}
            src={params.row.Product.ImageURL}
          />
        );
      },
    },
    {
      field: "ProductName",
      headerName: "Product",
      width: 200,
      valueGetter: (params) => `${params.row.Product.ProductName}`,
    },
    {
      field: "Price",
      headerName: "Price",
      width: 150,

      valueGetter: (params) => `${params.row.Product.Price}`,
    },
    {
      field: "CartPrice",
      headerName: "Total",
      type: "number",
      width: 100,

      renderCell: (params) => {
        const price = counterValue;
        return (
          <div>
            <p>
              {params.id === rowId
                ? params.row.Product.Price * price
                : params.row.CartPrice}
            </p>
          </div>
        );
      },
    },
  ];

  const rowHeight = () => {
    return 85.5;
  };
  return (
    <Box sx={{ height: 400, width: 900 }}>
      <DataGrid
        rows={cartItems ? cartItems : []}
        columns={columns}
        getRowHeight={rowHeight}
        sx={{
          "& .css-wop1k0-MuiDataGrid-footerContainer": {
            display: "none",
          },
        }}
        disableRowSelectionOnClick
        disableColumnSelector
        disableColumnMenu
        disableDensitySelector
        disableColumnFilter
        disableVirtualization
        rowSelection={false}
      />
    </Box>
  );
}
