import joblib
model_pretrained = joblib.load('Mushroom-rfc.pkl')
import numpy as np
 
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
def formPage():
    return render_template('Mushroom.html')

@app.route("/submit", methods=['POST'])
def submit():
    if request.method == 'POST':
        form_data = request.form
        
        # cap_shape
        cap_shape_bell = ''
        cap_shape_conical = ''
        cap_shape_convex = ''
        cap_shape_flat = ''
        cap_shape_knobbed = ''
        cap_shape_sunken = ''
        if form_data['cap_shape'] ==  'bell':
            cap_shape_bell = 'selected'
        elif form_data['cap_shape'] == 'conical':
            cap_shape_conical = 'selected'
        elif form_data['cap_shape'] == 'convex':
            cap_shape_convex = 'selected'
        elif form_data['cap_shape'] == 'flat':
            cap_shape_flat = 'selected'  
        elif form_data['cap_shape'] == 'knobbed':
            cap_shape_knobbed = 'selected'   
        elif form_data['cap_shape'] == 'sunken':
            cap_shape_sunken = 'selected' 
        

        
        # 轉換成數字
        form_data["cap_shape"] = (form_data["cap_shape"]).astype('int')
        form_data["cap_surface"] = (form_data["cap_surface"]).astype('int')
        form_data["cap_color"] = (form_data["cap_color"]).astype('int')
        form_data["bruises"] = (form_data["bruises"]).astype('int')
        form_data["odor"] = (form_data["odor"]).astype('int')
        form_data["gill_attachment"] = (form_data["gill_attachment"]).astype('int')
        form_data["gill_spacing"] = (form_data["gill_spacing"]).astype('int')
        form_data["gill_size"] = (form_data["gill_size"]).astype('int')
        form_data["gill_color"] = (form_data["gill_color"]).astype('int')
        form_data["stalk_shape"] = (form_data["stalk_shape"]).astype('int')
        form_data["stalk_root"] = (form_data["stalk_root"]).astype('int')
        form_data["stalk_surface_above_ring"] = (form_data["stalk_surface_above_ring"]).astype('int')
        form_data["stalk_surface_below_ring"] = (form_data["stalk_surface_below_ring"]).astype('int')
        form_data["stalk_color_above_ring"] = (form_data["stalk_color_above_ring"]).astype('int')
        form_data["stalk_color_below_ring"] = (form_data["stalk_color_below_ring"]).astype('int')
        form_data["veil_type"] = (form_data["veil_type"]).astype('int')
        form_data["veil_color"] = (form_data["veil_color"]).astype('int')
        form_data["ring_number"] = (form_data["ring_number"]).astype('int')
        form_data["ring_type"] = (form_data["ring_type"]).astype('int')
        form_data["spore_print_color"] = (form_data["spore_print_color"]).astype('int')
        form_data["population"] = (form_data["population"]).astype('int')
        form_data["habitat"] = (form_data["habitat"]).astype('int')

        # 套用模型
        result = model_pretrained.predict([[form_data["cap_shape"], form_data["cap_surface"], form_data["cap_color"], form_data["bruises"],
                                            form_data["odor"], form_data["gill_attachment"], form_data["gill_spacing"], form_data["gill_size"],
                                            form_data["gill_color"], form_data["stalk_shape"], form_data["stalk_root"], form_data["stalk_surface_above_ring"], 
                                            form_data["stalk_surface_below_ring"], form_data["stalk_color_above_ring"], form_data["stalk_color_below_ring"], 
                                            form_data["veil_type"], form_data["veil_color"], form_data["ring_number"], form_data["ring_type"], 
                                            form_data["spore_print_color"], form_data["population"], form_data["habitat"]]])
        
        result_proba = model_pretrained.predict_proba([[form_data["cap_shape"], form_data["cap_surface"], form_data["cap_color"], form_data["bruises"],
                                                        form_data["odor"], form_data["gill_attachment"], form_data["gill_spacing"], form_data["gill_size"],
                                                        form_data["gill_color"], form_data["stalk_shape"], form_data["stalk_root"], form_data["stalk_surface_above_ring"], 
                                                        form_data["stalk_surface_below_ring"], form_data["stalk_color_above_ring"], form_data["stalk_color_below_ring"], 
                                                        form_data["veil_type"], form_data["veil_color"], form_data["ring_number"], form_data["ring_type"], 
                                                        form_data["spore_print_color"], form_data["population"], form_data["habitat"]]])
        
        
        print(f'Result:{result}')
        print(f'Result_Proba:{result_proba}')
        if result[0] == 1:
            prediction = f'可食用(edible) - 系統信心 {result_proba[0][1]:.10f}'
        else:
            prediction = f'有毒(poisonous) - 系統信心 {result_proba[0][0]:.10f}'
        return render_template('Mushroom.html', 
        prediction = prediction)
 
if __name__ == "__main__":
    app.run()