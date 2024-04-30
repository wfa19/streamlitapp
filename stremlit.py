#!pip install git+https://github.com/wfa19/myMLpackage.git
from myMLpackage.general_utility import *
from myMLpackage.Data_preparations import *
from myMLpackage.scaling_and_transformation import *
from myMLpackage.feature_engineering import *
from myMLpackage.feature_selection import *
from myMLpackage.modelling import *
from myMLpackage.prediction import *
from myMLpackage.streamlit_wraparounds import *
import shutil
import tempfile

# the app

def main():
    st.title("Automated ML training")

    # Upload dataset
    st.header("Upload Dataset")
    uploaded_file = st.file_uploader("Browse file")
  

    if uploaded_file is not None:
        print(uploaded_file.name)
        data =load_data_stream(uploaded_file,uploaded_file.name)
        # Set up PyCaret
        st.header("Dataset Overview")
        st.write("Data info:")
        data_info = st.empty()
        data_info.write(calculate_variable_info(data))
        st.write("sample Data:")
        sample_data=st.empty()
        sample_data.write(data.head())
        
        # Sidebar inputs
        st.sidebar.header("Settings")
        
        # first configure datatypes
        dtyps=dtypess1(data)
        target=render_target(data)
        if target is not None:
           data=process_target1(data,target,data_info,sample_data)
           ignored_features = dtyps.get('ignore_features', [])
           selected_columns = [col for col in data.columns if col not in (ignored_features or []) and col != target]
           missing=data[selected_columns].isnull().sum()
           imputations=process_missing1(missing)
           outlier=process_outliers1()
           fix_imba=fix_imbalances1()
           norm=normalizer1()
           tran=transformations1()
           target_trans=target_transformation1(data,target,dtyps)
           feat_eng=feature_engineering1(data)
           feat_sel=feature_select1()
           
        to_target=st.sidebar.button("submit")
        cat_tune=None
        if to_target:
           settings=setup_pycaret(data,target,False,dtyps,imputations,outlier,fix_imba,norm,tran,target_trans,feat_eng,feat_sel)
           
           modeltype=model_typ(data,target,dtyps)
           if modeltype=='classification':
              st.write("Distribution of {}".format(target))
              st.pyplot(plot_countplot(data,target,hue=target,xlabel= "{}".format(target), ylabel='count', title="A bar graph of the {} Variable".format(target)))
              settingsinfo=classification.pull(settings)
              best_model=model_comparisons(modeltype)
              comparisons=classification.pull(best_model)
              cat_tune = tuned_model(best_model,modeltype)
              tunedresults=classification.pull(cat_tune)
           else:
             st.write("Distribution of {}".format(target))
             st.pyplot(plot_histogram(data, target, bins=50))
             settingsinfo=regression.pull(settings)
             best_model=model_comparisons(modeltype)
             comparisons=regression.pull(best_model)
             cat_tune = tuned_model(best_model,modeltype)
             tunedresults=regression.pull(cat_tune)
           st.write("Correlation plot")
           st.pyplot(plot_correlation_matrix(data, dtyps))
           st.header("Modelling")
           st.write("Set up information:",settingsinfo)
           st.write("Model Comparisons:",comparisons)
           st.write("Best Model performance:",tunedresults)
           if target in  (dtyps['categorical_features'] or []) or data[target].dtype == 'object':
              img=classification.plot_model(cat_tune,plot='feature',save=True)
           else:
             img=regression.plot_model(cat_tune,plot='feature',save=True)
           st.write('feature importance:')
           st.image(img)
           
           if modeltype=='classification':
              saved_mod=classification.save_model(cat_tune,'best_pipeline')
           else:
              saved_mod=regression.save_model(cat_tune,'best_pipeline')
              
           model_path='best_pipeline.pkl'
           temp_dir = tempfile.mkdtemp(prefix="pycaret_model_")
           shutil.copy(model_path, temp_dir)
           
           shutil.make_archive(temp_dir, "zip",temp_dir)
           with open(f"{temp_dir}.zip", "rb") as f:
                db = f.read()
           st.header("Download trained model")
           st.download_button("Download model", data=db, file_name="best_pipeline.zip")
           #prediction
           #prediction1(cat_tune)
              
if __name__ == "__main__":
    main()
