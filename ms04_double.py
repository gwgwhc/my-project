from iqtools import *
import plotly.graph_objects as go
from plotly.subplots import make_subplots
matplotlib.use('TkAgg')  # stop matplotlib running in backend

# import data
directory = 'physics/spectrum_analysis'
filename = f'{directory}/tiqfiles/fumikara.tiq'

# initialise iqtools
iqdata = get_iq_object(filename)
print(f"""nsamples: {iqdata.nsamples_total} 
sample frequency: {iqdata.fs}""")

# binning
lframes = 4000  # number of bins
# setting nframes to match number of bins over data
nframes = int(iqdata.nsamples_total/lframes)
iqdata.read(nframes, lframes)

# plot 1 data
xx, yy, zz = iqdata.get_spectrogram(nframes=nframes, lframes=lframes)

# plot 2 data
lframes = 1000
nframes = int(iqdata.nsamples_total/lframes)
iqdata.read(nframes, lframes)
xxx, yyy, zzz = iqdata.get_spectrogram(nframes=nframes, lframes=lframes)

# --------- plotting ----------
# plot 1
fig = make_subplots(rows=2, cols=1)
fig.add_trace(go.Heatmap(
    z=zz,
    x=xx[0, :],
    y=yy[:, 0],
    colorscale='jet',
    colorbar=dict(
    outlinewidth=1,
    title='Power Spectral Density',
    titleside='right',
    titlefont_size=20,
    tickfont_size=16
    )),          
    row=1, col=1
)

# plot 2
fig.add_trace(go.Heatmap(
    z=zzz,
    x=xxx[0, :],
    y=yyy[:, 0],
    colorscale='jet',
    showscale=False, # hide colorbar
    ),
    row=2, col=1
)

axis_template = dict(
    ticks='outside',
    nticks=10,
    titlefont_size=20,
    tickfont_size=16
)

# fig.update_layout(
#     height=800,
#     width=1200,
    
#     xaxis=axis_template | dict(
#         title_text="Frequency (kHz)"
#     ),

#     yaxis=axis_template | dict(
#         title_text="Time (s)"
#     ),
# )

fig.show()
# fig.write_image(f'{directory}/plots/test.pdf')
