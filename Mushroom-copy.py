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

        # cap-shape
        cap_shape_b = ''
        cap_shape_c = ''
        cap_shape_x = ''
        cap_shape_f = ''
        cap_shape_k = ''
        cap_shape_s = ''
        if form_data['cap_shape'] == '0':
            cap_shape_b = 'selected'
        elif form_data['cap_shape'] == '1':
            cap_shape_c = 'selected'
        elif form_data['cap_shape'] == '2':
            cap_shape_x = 'selected'
        elif form_data['cap_shape'] == '3':
            cap_shape_f = 'selected'  
        elif form_data['cap_shape'] == '4':
            cap_shape_k = 'selected'   
        elif form_data['cap_shape'] == '5':
            cap_shape_s = 'selected'
        
        #cap-surface
        cap_surface_f = ''
        cap_surface_g = ''
        cap_surface_y = ''
        cap_surface_s = ''
        if form_data['cap_surface'] == '0':
            cap_surface_f = 'selected'
        elif form_data['cap_surface'] == '1':
            cap_surface_g = 'selected'
        elif form_data['cap_surface'] == '2':
            cap_surface_y = 'selected'
        elif form_data['cap_surface'] == '3':
            cap_surface_s = 'selected'  
        
        #cap_color
        cap_color_n = ''
        cap_color_b = ''
        cap_color_c = ''
        cap_color_g = ''
        cap_color_r = ''
        cap_color_p = ''
        cap_color_u = ''
        cap_color_e = ''
        cap_color_w = ''
        cap_color_y = ''
        if form_data['cap_color'] == '0':
            cap_color_n = 'selected'
        elif form_data['cap_color'] == '1':
            cap_color_b = 'selected'
        elif form_data['cap_color'] == '2':
            cap_color_c = 'selected'
        elif form_data['cap_color'] == '3':
            cap_color_g = 'selected'
        elif form_data['cap_color'] == '4':
            cap_color_r = 'selected'
        elif form_data['cap_color'] == '5':
            cap_color_p = 'selected'
        elif form_data['cap_color'] == '6':
            cap_color_u = 'selected'
        elif form_data['cap_color'] == '7':
            cap_color_e = 'selected'
        elif form_data['cap_color'] == '8':
            cap_color_w = 'selected'
        elif form_data['cap_color'] == '9':
            cap_color_y = 'selected'

        #bruises
        bruises_t = ''
        bruises_f = ''
        if form_data['bruises'] == '1':
            bruises_t = 'selected'
        elif form_data['bruises'] == '0':
            bruises_f = 'selected'

        #odor
        odor_a = ''
        odor_l = ''
        odor_c = ''
        odor_y = ''
        odor_f = ''
        odor_m = ''
        odor_n = ''
        odor_p = ''
        odor_s = ''
        if form_data['odor'] == '0':
            odor_a = 'selected'
        elif form_data['odor'] == '1':
            odor_l = 'selected'
        elif form_data['odor'] == '2':
            odor_c = 'selected'
        elif form_data['odor'] == '3':
            odor_y = 'selected'
        elif form_data['odor'] == '4':
            odor_f = 'selected'
        elif form_data['odor'] == '5':
            odor_m = 'selected'
        elif form_data['odor'] == '6':
            odor_n = 'selected'
        elif form_data['odor'] == '7':
            odor_p = 'selected'
        elif form_data['odor'] == '8':
            odor_s = 'selected'

        #gill_attachment
        gill_attachment_a = ''
        gill_attachment_d = ''
        gill_attachment_f = ''
        gill_attachment_n = ''
        if form_data['gill_attachment'] == '0':
            gill_attachment_a = 'selected'
        elif form_data['gill_attachment'] == '1':
            gill_attachment_d = 'selected'
        elif form_data['gill_attachment'] == '2':
            gill_attachment_f = 'selected'
        elif form_data['gill_attachment'] == '3':
            gill_attachment_n = 'selected'

        #gill_spacing
        gill_spacing_c = ''
        gill_spacing_w = ''
        gill_spacing_d = ''
        if form_data['gill_spacing'] == '0':
            gill_spacing_c = 'selected'
        elif form_data['gill_spacing'] == '1':
            gill_spacing_w = 'selected'
        elif form_data['gill_spacing'] == '2':
            gill_spacing_d = 'selected'

        #gill_size
        gill_size_b = ''
        gill_size_n = ''
        if form_data['gill_size'] == '0':
            gill_size_b = 'selected'
        elif form_data['gill_size'] == '1':
            gill_size_n = 'selected'
        
        #gill_color
        gill_color_k = ''
        gill_color_n = ''
        gill_color_b = ''
        gill_color_h = ''
        gill_color_g = ''
        gill_color_r = ''
        gill_color_o = ''
        gill_color_p = ''
        gill_color_u = ''
        gill_color_e = ''
        gill_color_w = ''
        gill_color_y = ''
        if form_data['gill_color'] == '0':
            gill_color_k = 'selected'
        elif form_data['gill_color'] == '1':
            gill_color_n = 'selected'
        elif form_data['gill_color'] == '2':
            gill_color_b = 'selected'
        elif form_data['gill_color'] == '3':
            gill_color_h = 'selected'
        elif form_data['gill_color'] == '4':
            gill_color_g = 'selected'
        elif form_data['gill_color'] == '5':
            gill_color_r = 'selected'
        elif form_data['gill_color'] == '6':
            gill_color_o = 'selected'
        elif form_data['gill_color'] == '7':
            gill_color_p = 'selected'
        elif form_data['gill_color'] == '8':
            gill_color_u = 'selected'
        elif form_data['gill_color'] == '9':
            gill_color_e = 'selected'
        elif form_data['gill_color'] == '10':
            gill_color_w = 'selected'
        elif form_data['gill_color'] == '11':
            gill_color_y = 'selected'

        #stalk_shape
        stalk_shape_e = ''
        stalk_shape_t = ''
        if form_data['stalk_shape'] == '0':
            stalk_shape_e = 'selected'
        elif form_data['stalk_shape'] == '1':
            stalk_shape_t = 'selected'

        #stalk_root
        stalk_root_b = ''
        stalk_root_c = ''
        stalk_root_u = ''
        stalk_root_e = ''
        stalk_root_z = ''
        stalk_root_r = ''
        stalk_root_Na = ''
        if form_data['stalk_root'] == '0':
            stalk_root_b = 'selected'
        elif form_data['stalk_root'] == '1':
            stalk_root_c = 'selected'
        elif form_data['stalk_root'] == '2':
            stalk_root_u = 'selected'
        elif form_data['stalk_root'] == '3':
            stalk_root_e = 'selected'
        elif form_data['stalk_root'] == '4':
            stalk_root_z = 'selected'
        elif form_data['stalk_root'] == '5':
            stalk_root_r = 'selected'
        elif form_data['stalk_root'] == '6':
            stalk_root_Na = 'selected'

        #stalk_surface_above_ring
        stalk_surface_above_ring_f = ''
        stalk_surface_above_ring_y = ''
        stalk_surface_above_ring_k = ''
        stalk_surface_above_ring_s = ''
        if form_data['stalk_surface_above_ring'] == '0':
            stalk_surface_above_ring_f = 'selected'
        elif form_data['stalk_surface_above_ring'] == '1':
            stalk_surface_above_ring_y = 'selected'
        elif form_data['stalk_surface_above_ring'] == '2':
            stalk_surface_above_ring_k = 'selected'
        elif form_data['stalk_surface_above_ring'] == '3':
            stalk_surface_above_ring_s = 'selected'

        #stalk_surface_below_ring
        stalk_surface_below_ring_f = ''
        stalk_surface_below_ring_y = ''
        stalk_surface_below_ring_k = ''
        stalk_surface_below_ring_s = ''
        if form_data['stalk_surface_below_ring'] == '0':
            stalk_surface_below_ring_f = 'selected'
        elif form_data['stalk_surface_below_ring'] == '1':
            stalk_surface_below_ring_y = 'selected'
        elif form_data['stalk_surface_below_ring'] == '2':
            stalk_surface_below_ring_k = 'selected'
        elif form_data['stalk_surface_below_ring'] == '3':
            stalk_surface_below_ring_s = 'selected'

        #stalk_color_above_ring
        stalk_color_above_ring_n = ''
        stalk_color_above_ring_b = ''
        stalk_color_above_ring_c = ''
        stalk_color_above_ring_g = ''
        stalk_color_above_ring_o = ''
        stalk_color_above_ring_p = ''
        stalk_color_above_ring_e = ''
        stalk_color_above_ring_w = ''
        stalk_color_above_ring_y = ''
        if form_data['stalk_color_above_ring'] == '0':
            stalk_color_above_ring_n = 'selected'
        elif form_data['stalk_color_above_ring'] == '1':
            stalk_color_above_ring_b = 'selected'
        elif form_data['stalk_color_above_ring'] == '2':
            stalk_color_above_ring_c = 'selected'
        elif form_data['stalk_color_above_ring'] == '3':
            stalk_color_above_ring_g = 'selected'
        elif form_data['stalk_color_above_ring'] == '4':
            stalk_color_above_ring_o = 'selected'
        elif form_data['stalk_color_above_ring'] == '5':
            stalk_color_above_ring_p = 'selected'
        elif form_data['stalk_color_above_ring'] == '6':
            stalk_color_above_ring_e = 'selected'
        elif form_data['stalk_color_above_ring'] == '7':
            stalk_color_above_ring_w = 'selected'
        elif form_data['stalk_color_above_ring'] == '8':
            stalk_color_above_ring_y = 'selected'                

        #stalk_color_below_ring
        stalk_color_below_ring_n = ''
        stalk_color_below_ring_b = ''
        stalk_color_below_ring_c = ''
        stalk_color_below_ring_g = ''
        stalk_color_below_ring_o = ''
        stalk_color_below_ring_p = ''
        stalk_color_below_ring_e = ''
        stalk_color_below_ring_w = ''
        stalk_color_below_ring_y = ''
        if form_data['stalk_color_below_ring'] == '0':
            stalk_color_below_ring_n = 'selected'
        elif form_data['stalk_color_below_ring'] == '1':
            stalk_color_below_ring_b = 'selected'
        elif form_data['stalk_color_below_ring'] == '2':
            stalk_color_below_ring_c = 'selected'
        elif form_data['stalk_color_below_ring'] == '3':
            stalk_color_below_ring_g = 'selected'
        elif form_data['stalk_color_below_ring'] == '4':
            stalk_color_below_ring_o = 'selected'
        elif form_data['stalk_color_below_ring'] == '5':
            stalk_color_below_ring_p = 'selected'
        elif form_data['stalk_color_below_ring'] == '6':
            stalk_color_below_ring_e = 'selected'
        elif form_data['stalk_color_below_ring'] == '7':
            stalk_color_below_ring_w = 'selected'
        elif form_data['stalk_color_below_ring'] == '8':
            stalk_color_below_ring_y = 'selected'     

        #veil_type
        veil_type_p = ''
        veil_type_u = ''
        if form_data['veil_type'] == '1':
            veil_type_p = 'selected'
        elif form_data['veil_type'] == '0':
            veil_type_u = 'selected'

        #veil_color
        veil_color_n = ''
        veil_color_o = ''
        veil_color_w = ''
        veil_color_y = ''
        if form_data['veil_color'] == '0':
            veil_color_n = 'selected'
        elif form_data['veil_color'] == '1':
            veil_color_o = 'selected'
        elif form_data['veil_color'] == '2':
            veil_color_w = 'selected'
        elif form_data['veil_color'] == '3':
            veil_color_y = 'selected'

        #ring_number
        ring_number_n = ''
        ring_number_o = ''
        ring_number_t = ''
        if form_data['ring_number'] == '0':
            ring_number_n = 'selected'
        elif form_data['ring_number'] == '1':
            ring_number_o = 'selected'
        elif form_data['ring_number'] == '2':
            ring_number_t = 'selected'
        
        #ring_type
        ring_type_c = ''
        ring_type_e = ''
        ring_type_f = ''
        ring_type_l = ''
        ring_type_n = ''
        ring_type_p = ''
        ring_type_s = ''
        ring_type_z = ''
        if form_data['ring_type'] == '0':
            ring_type_c = 'selected'
        elif form_data['ring_type'] == '1':
            ring_type_e = 'selected'
        elif form_data['ring_type'] == '2':
            ring_type_f = 'selected'
        elif form_data['ring_type'] == '3':
            ring_type_l = 'selected'
        elif form_data['ring_type'] == '4':
            ring_type_n = 'selected'
        elif form_data['ring_type'] == '5':
            ring_type_p = 'selected'
        elif form_data['ring_type'] == '6':
            ring_type_s = 'selected'
        elif form_data['ring_type'] == '7':
            ring_type_z = 'selected'

        #spore_print_color
        spore_print_color_k = ''
        spore_print_color_n = ''
        spore_print_color_b = ''
        spore_print_color_h = ''
        spore_print_color_r = ''
        spore_print_color_o = ''
        spore_print_color_u = ''
        spore_print_color_w = ''
        spore_print_color_y = ''
        if form_data['spore_print_color'] == '0':
            spore_print_color_k = 'selected'
        elif form_data['spore_print_color'] == '1':
            spore_print_color_n = 'selected'
        elif form_data['spore_print_color'] == '2':
            spore_print_color_b = 'selected'
        elif form_data['spore_print_color'] == '3':
            spore_print_color_h = 'selected'
        elif form_data['spore_print_color'] == '4':
            spore_print_color_r = 'selected'
        elif form_data['spore_print_color'] == '5':
            spore_print_color_o = 'selected'
        elif form_data['spore_print_color'] == '6':
            spore_print_color_u = 'selected'
        elif form_data['spore_print_color'] == '7':
            spore_print_color_w = 'selected'
        elif form_data['spore_print_color'] == '8':
            spore_print_color_y = 'selected'

        #population
        population_a = ''
        population_c = ''
        population_n = ''
        population_s = ''
        population_v = ''
        population_y = ''
        if form_data['population'] == '0':
            population_a = 'selected' 
        elif form_data['population'] == '1':
            population_c = 'selected' 
        elif form_data['population'] == '2':
            population_n = 'selected' 
        elif form_data['population'] == '3':
            population_s = 'selected' 
        elif form_data['population'] == '4':
            population_v = 'selected' 
        elif form_data['population'] == '5':
            population_y = 'selected' 

        #habitat
        habitat_g = ''
        habitat_l = ''
        habitat_m = ''
        habitat_p = ''
        habitat_u = ''
        habitat_w = ''
        habitat_d = ''
        if form_data['habitat'] == '0':
            habitat_g = 'selected'
        elif form_data['habitat'] == '1':
            habitat_l = 'selected'
        elif form_data['habitat'] == '2':
            habitat_m = 'selected'
        elif form_data['habitat'] == '3':
            habitat_p = 'selected'
        elif form_data['habitat'] == '4':
            habitat_u = 'selected'
        elif form_data['habitat'] == '5':
            habitat_w = 'selected'
        elif form_data['habitat'] == '6':
            habitat_d = 'selected'


        # 套用模型
        result = model_pretrained.predict([[int(form_data["cap_shape"]), int(form_data["cap_surface"]), int(form_data["cap_color"]), int(form_data["bruises"]),
                                            int(form_data["odor"]), int(form_data["gill_attachment"]), int(form_data["gill_spacing"]), int(form_data["gill_size"]),
                                            int(form_data["gill_color"]), int(form_data["stalk_shape"]), int(form_data["stalk_root"]), int(form_data["stalk_surface_above_ring"]), 
                                            int(form_data["stalk_surface_below_ring"]), int(form_data["stalk_color_above_ring"]), int(form_data["stalk_color_below_ring"]), 
                                            int(form_data["veil_type"]), int(form_data["veil_color"]), int(form_data["ring_number"]), int(form_data["ring_type"]), 
                                            int(form_data["spore_print_color"]), int(form_data["population"]), int(form_data["habitat"])]])
        
        result_proba = model_pretrained.predict_proba([[int(form_data["cap_shape"]), int(form_data["cap_surface"]), int(form_data["cap_color"]), int(form_data["bruises"]),
                                                        int(form_data["odor"]), int(form_data["gill_attachment"]), int(form_data["gill_spacing"]), int(form_data["gill_size"]),
                                                        int(form_data["gill_color"]), int(form_data["stalk_shape"]), int(form_data["stalk_root"]), int(form_data["stalk_surface_above_ring"]), 
                                                        int(form_data["stalk_surface_below_ring"]), int(form_data["stalk_color_above_ring"]), int(form_data["stalk_color_below_ring"]), 
                                                        int(form_data["veil_type"]), int(form_data["veil_color"]), int(form_data["ring_number"]), int(form_data["ring_type"]), 
                                                        int(form_data["spore_print_color"]), int(form_data["population"]), int(form_data["habitat"])]])
        
        
        print(f'Result:{result}')
        print(f'Result_Proba:{result_proba}')
        if result[0] == 1:
            prediction = f'可食用(edible) - 系統信心 {result_proba[0][1]:.10f}'
        else:
            prediction = f'有毒(poisonous) - 系統信心 {result_proba[0][0]:.10f}'
        return render_template('Mushroom.html', 
        cap_shape_b = cap_shape_b,
        cap_shape_c = cap_shape_c,
        cap_shape_x = cap_shape_x,
        cap_shape_f = cap_shape_f,
        cap_shape_k = cap_shape_k,
        cap_shape_s = cap_shape_s,
        cap_surface_f = cap_surface_f,
        cap_surface_g = cap_surface_g,
        cap_surface_y = cap_surface_y,
        cap_surface_s = cap_surface_s, 
        cap_color_n = cap_color_n,
        cap_color_b = cap_color_b,
        cap_color_c = cap_color_c,
        cap_color_g = cap_color_g,
        cap_color_r = cap_color_r,
        cap_color_p = cap_color_p,
        cap_color_u = cap_color_u,
        cap_color_e = cap_color_e,
        cap_color_w = cap_color_w,
        cap_color_y = cap_color_y,        
        bruises_t = bruises_t,
        bruises_f = bruises_f,
        odor_a = odor_a,
        odor_l = odor_l,
        odor_c = odor_c,
        odor_y = odor_y,
        odor_f = odor_f,
        odor_m = odor_m,
        odor_n = odor_n,
        odor_p = odor_p,
        odor_s = odor_s,
        gill_attachment_a = gill_attachment_a,
        gill_attachment_d = gill_attachment_d,
        gill_attachment_f = gill_attachment_f,
        gill_attachment_n = gill_attachment_n,
        gill_spacing_c = gill_spacing_c,
        gill_spacing_w = gill_spacing_w,
        gill_spacing_d = gill_spacing_d,
        gill_size_b = gill_size_b,
        gill_size_n = gill_size_n,
        gill_color_k = gill_color_k,
        gill_color_n = gill_color_n,
        gill_color_b = gill_color_b,
        gill_color_h = gill_color_h,
        gill_color_g = gill_color_g,
        gill_color_r = gill_color_r,
        gill_color_o = gill_color_o,
        gill_color_p = gill_color_p,
        gill_color_u = gill_color_u,
        gill_color_e = gill_color_e,
        gill_color_w = gill_color_w,
        gill_color_y = gill_color_y,
        stalk_shape_e = stalk_shape_e,
        stalk_shape_t = stalk_shape_t,
        stalk_root_b = stalk_root_b,
        stalk_root_c = stalk_root_c,
        stalk_root_u = stalk_root_u,
        stalk_root_e = stalk_root_e,
        stalk_root_z = stalk_root_z,
        stalk_root_r = stalk_root_r,
        stalk_root_Na = stalk_root_Na,
        stalk_surface_above_ring_f = stalk_surface_above_ring_f,
        stalk_surface_above_ring_y = stalk_surface_above_ring_y,
        stalk_surface_above_ring_k = stalk_surface_above_ring_k,
        stalk_surface_above_ring_s = stalk_surface_above_ring_s,
        stalk_surface_below_ring_f = stalk_surface_below_ring_f,
        stalk_surface_below_ring_y = stalk_surface_below_ring_y,
        stalk_surface_below_ring_k = stalk_surface_below_ring_k,
        stalk_surface_below_ring_s = stalk_surface_below_ring_s,
        stalk_color_above_ring_n = stalk_color_above_ring_n,
        stalk_color_above_ring_b = stalk_color_above_ring_b,
        stalk_color_above_ring_c = stalk_color_above_ring_c,
        stalk_color_above_ring_g = stalk_color_above_ring_g,
        stalk_color_above_ring_o = stalk_color_above_ring_o,
        stalk_color_above_ring_p = stalk_color_above_ring_p,
        stalk_color_above_ring_e = stalk_color_above_ring_e,
        stalk_color_above_ring_w = stalk_color_above_ring_w,
        stalk_color_above_ring_y = stalk_color_above_ring_y,
        stalk_color_below_ring_n = stalk_color_below_ring_n,
        stalk_color_below_ring_b = stalk_color_below_ring_b,
        stalk_color_below_ring_c = stalk_color_below_ring_c,
        stalk_color_below_ring_g = stalk_color_below_ring_g,
        stalk_color_below_ring_o = stalk_color_below_ring_o,
        stalk_color_below_ring_p = stalk_color_below_ring_p,
        stalk_color_below_ring_e = stalk_color_below_ring_e,
        stalk_color_below_ring_w = stalk_color_below_ring_w,
        stalk_color_below_ring_y = stalk_color_below_ring_y,
        veil_type_p = veil_type_p,
        veil_type_u = veil_type_u,
        veil_color_n =veil_color_n,
        veil_color_o =veil_color_o,
        veil_color_w = veil_color_w,
        veil_color_y = veil_color_y,
        ring_number_n = ring_number_n,
        ring_number_o = ring_number_o,
        ring_number_t = ring_number_t,
        ring_type_c = ring_type_c,
        ring_type_e = ring_type_e,
        ring_type_f = ring_type_f,
        ring_type_l = ring_type_l,
        ring_type_n = ring_type_n,
        ring_type_p = ring_type_p,
        ring_type_s = ring_type_s,
        ring_type_z = ring_type_z,
        spore_print_color_k = spore_print_color_k,
        spore_print_color_n = spore_print_color_n,
        spore_print_color_b = spore_print_color_b,
        spore_print_color_h = spore_print_color_h,
        spore_print_color_r = spore_print_color_r,
        spore_print_color_o = spore_print_color_o,
        spore_print_color_u = spore_print_color_u,
        spore_print_color_w = spore_print_color_w,
        spore_print_color_y = spore_print_color_y,
        population_a = population_a,
        population_c = population_c,
        population_n = population_n,
        population_s = population_s,
        population_v = population_v,
        population_y = population_y,
        habitat_g = habitat_g,
        habitat_l = habitat_l,
        habitat_m = habitat_m,
        habitat_p = habitat_p,
        habitat_u = habitat_u,
        habitat_w = habitat_w,
        habitat_d = habitat_d,
        prediction = prediction)
 
if __name__ == "__main__":
    app.run()