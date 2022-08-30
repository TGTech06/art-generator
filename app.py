import os
import sys



#clone https://github.com/openai/CLIP
os.system("git clone https://github.com/openai/CLIP")
os.system("git clone https://github.com/CompVis/taming-transformers.git")
# !pip install taming-transformers
#clone https://github.com/CompVis/taming-transformers.git
os.system("git clone https://github.com/dribnet/pixray")
try:
    os.mkdir("steps")
    os.mkdir("models")
except:
    print("Already exists")
    
import streamlit as st
import torch
sys.path.append("pixray")
import pixray



# Define the main function
def generate(prompt, quality, aspect):
    torch.cuda.empty_cache()
    pixray.reset_settings()
    
    # use_pixeldraw = (style == 'pixel art')
    # use_clipdraw = (style == 'painting')
    pixray.add_settings(prompts=prompt,
                        aspect=aspect,
                        iterations=50,
                        quality=quality,
                        make_video=False)
  
    settings = pixray.apply_settings()
    pixray.do_init(settings)
    pixray.do_run(settings)

    return 'output.png'

# # Create the UI with Gradio
# prompt = gr.inputs.Textbox(default="Underwater city", label="Text Prompt")
# quality = gr.inputs.Radio(choices=['draft', 'normal', 'better'], label="Quality")
# # style = gr.inputs.Radio(choices=['image', 'painting','pixel art'], label="Type")
# aspect = gr.inputs.Radio(choices=['square', 'widescreen','portrait'], label="Size")


# iface = gr.Interface(generate, inputs=[prompt, quality, aspect], outputs=['image'], enable_queue=True, live=False)
# iface.launch(debug=False)


# Create the UI with streamlit
import streamlit as st
st.write('# Art Generator')
st.write('## Hi I am an artistic AI 👋🏻 ')
st.markdown("## Text Prompt:")
prompt = st.text_input('Prompt')
quality = 'normal'
style = 'image'
aspect = 'widescreen'
btnResult = st.button('Generate')
if btnResult:

    with st.spinner('Drawing...'):
        image = generate(prompt, quality, aspect)
        st.image(image)
    st.write('## Should be done!')