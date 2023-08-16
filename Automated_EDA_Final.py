import pandas as pd
import matplotlib.pyplot as plt

# Function to load data from different file formats
def load_data(file_path):
    try:
        if file_path.endswith('.csv'):
            data = pd.read_csv(file_path)
        elif file_path.endswith('.xlsx'):
            data = pd.read_excel(file_path)
        elif file_path.endswith('.db'):
            # Load data from SQL database
            # Use appropriate SQL library to connect and fetch data
            data = None
        else:
            raise ValueError("Unsupported file format")
    except Exception as e:
        print(e)
        return None

    return data

# Function to preprocess the loaded data
def preprocess_data(data):
    # Generate summary statistics
    summary = data.describe()
    print(summary)
    
    # Handle missing values
    data = data.dropna()
    
    # Handle data types
    column_types = data.dtypes
    
    # Encode categorical features
    for column in data.columns:
        if column_types[column] == 'object':
            data[column] = data[column].astype('category')
    
    # Scale numerical features
    for column in data.columns:
        if column_types[column] in ['float64', 'int64']:
            data[column] = data[column] / data[column].max()

    return data

# Function to create histograms for numerical columns
def visualize_histograms(data, bin_count):
    numerical_columns = data.select_dtypes(include=['float64', 'int64']).columns
    for column in numerical_columns:
        plt.figure(figsize=(8, 6))
        plt.hist(data[column], bins=bin_count, edgecolor='black', alpha=0.7)
        plt.title(f'Histogram of {column}')
        plt.xlabel(f'Value of {column}')
        plt.ylabel('Frequency')
        plt.grid(True)
        plt.show()

# Function to create scatter for numerical columns
       
def visualize_scatter(dataframe, x_column):
    numeric_columns = dataframe.select_dtypes(include=[pd.np.number]).columns
    y_columns = [col for col in numeric_columns if col != x_column]

    for y_col in y_columns:
        plt.figure(figsize=(8, 6))
        plt.scatter(dataframe[x_column], dataframe[y_col])
        plt.xlabel(x_column)
        plt.ylabel(y_col)
        plt.title(f'Scatter Plot: {y_col} vs {x_column}')
        plt.grid(True)
        plt.show()
####################################################################################################3333
def visualize_bar(data,subsetcolumn,value_tocount1,value_tocount2,columnaftersubset):

    male=data[data[subsetcolumn]==value_tocount1]
    #START
    maleN=male[columnaftersubset].value_counts()
    maleN_df=pd.DataFrame(maleN)
    #counts for female
    female=data[data[subsetcolumn]==value_tocount2]
    #START
    femaleN=female[columnaftersubset].value_counts()
    femaleN_df=pd.DataFrame(femaleN)

    plt.bar(maleN_df.index,maleN_df[columnaftersubset])
    plt.bar(femaleN_df.index,femaleN_df[columnaftersubset])
    plt.show()




# Main function
def main():
    file_path = input("Enter the path to the data file (CSV or Excel): ")
    data = load_data(file_path)
    
    if data is not None:
        preprocessed_data = preprocess_data(data)

    

    print("Choose an option:")
    print("1. Visualize histograms")
    print("2. scatter plots")
    print("3. Visualize bar plots")
    choice = int(input("Enter your choice: "))

    if choice == 1:        
        bin_count = int(input("Enter the number of bins for the histogram: "))
        visualize_histograms(preprocessed_data, bin_count)

    elif choice == 2:
        x_column = input("Enter the column you want to scatter the data with: ")
        visualize_scatter(preprocessed_data, x_column)

    elif choice == 3:
        subsetcolumn=input("Enter subsetcolumn")
        value_tocount1=input("Enter value_tocount1")
        value_tocount2=input("Enter value_tocount2")
        columnaftersubset=input("Enter columnaftersubset ")
        visualize_bar(preprocessed_data,subsetcolumn,value_tocount1,value_tocount2,columnaftersubset) 
     


if __name__ == "__main__":
    main()
