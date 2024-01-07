import plotly.graph_objects as go
import numpy as np

dir = "results_daily_o365_inv_scaler_3layer"

test_pred = np.load(f"{dir}/test_pred.npy")[0]
test_true = np.load(f"{dir}/test_true.npy")[0]

# Create traces
fig = go.Figure()
fig.add_trace(go.Scatter(y=test_pred, mode='lines', name='pred'))
fig.add_trace(go.Scatter(y=test_true, mode='lines', name='true'))

# Update layout for better interaction
fig.update_layout(
    title='Interactive Test Predictions vs True Values',
    xaxis_title='X',
    yaxis_title='Y',
    hovermode="x unified"
)

fig.show()

# compute the MAE
mae = np.mean(np.abs(test_pred - test_true))
print(f"MAE: {mae}")

# compute the MAPE
mape = np.mean(np.abs((test_pred - test_true) / test_true))
print(f"MAPE: {mape}")

# compute the RMSE
rmse = np.sqrt(np.mean(np.square(test_pred - test_true)))
print(f"RMSE: {rmse}")

# compute the NRMSE
nrmse = rmse / np.mean(test_true)
print(f"NRMSE: {nrmse}")