from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Select the four features to scale
features_to_scale = ['Length', 'Recency', 'Frequency', 'StayingRate']

# Apply standard scaling (mean = 0, std = 1)
scaler = StandardScaler()
df_scaled[features_to_scale] = scaler.fit_transform(df_scaled[features_to_scale])

# Min-Max Scaling (Optional)
minmax_scaler = MinMaxScaler()
df_normalized = minmax_scaler.fit_transform(df_scaled[features_to_scale])