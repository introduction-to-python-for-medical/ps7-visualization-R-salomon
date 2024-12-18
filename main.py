data = fetch_openml(name='diabetes', version=1, as_frame=True)

features = list(df.columns)
print("Available features:", features)
selected_features = [features[0], features[2], features[5], features[6], features[7], features[8]]
print("Selected features: ", selected_features)

reference_feature = selected_features[1]
y = df[reference_feature]

fig, axs  = plt.subplots(1, len(selected_features), figsize = (20,3))

for ax, f in zip(axs, features):
  ax.scatter(df[f], y)
  ax.set_xlabel(f)

plt.show()


reference_feature = selected_features[2]  # The reference feature
comparison_feature = selected_features[0]  # A feature to compare to

# Create a scatter plot for the selected pair
plt.figure(figsize=(8, 6))
plt.scatter(df[reference_feature], df[comparison_feature], alpha=0.6)
plt.xlabel(reference_feature)
plt.ylabel(comparison_feature)

#Save the plot as an image file
plt.savefig('correlation_plot1.png')

plt.show()

