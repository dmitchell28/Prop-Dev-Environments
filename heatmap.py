import bqplot as bqp
import itertools
import ipywidgets as ipw

def plot_heat_map(df_heatmap):
    
    xlabel='' 
    ylabel = ''
    
    x_heatmap_scale,y_heatmap_scale,colour_scale = bqp.OrdinalScale(),bqp.OrdinalScale(reverse=True),bqp.ColorScale()
    
    x_heatmap_axis = bqp.Axis(scale=x_heatmap_scale,label=xlabel,grid_lines='none',side='top')
    y_heatmap_axis = bqp.Axis(scale=y_heatmap_scale,orientation='vertical',label=ylabel,grid_lines='none')
    color_axis = bqp.ColorAxis(scale=colour_scale,visible = False)
    
    lst_row_column = list(itertools.product(df_heatmap.index,df_heatmap.columns))
    
    trimmed_row_labels = [''.join([word[:4] for word in row.replace('_', ' ').split(' ')]) for row,column in lst_row_column]
    trimmed_column_labels = [''.join([word[:4] for word in column.replace('_', ' ').split(' ')]) for row,column in lst_row_column]
    lst_labels = [df_heatmap.loc[row,column].round(2)for row,column in lst_row_column]
    
    heatmap_tile_labels = bqp.Label(x=trimmed_column_labels,y=trimmed_row_labels,text=lst_labels,
                                    scales={'x': x_heatmap_scale, 'y': y_heatmap_scale},align='middle',colors=['black'])

    heatmap_marks = bqp.GridHeatMap(row=[''.join([word[:4] for word in header.split(' ')])for header in df_heatmap.index],
                                            column=[''.join([word[:4] for word in header.split(' ')]) for header in df_heatmap.columns],
                                            color=-df_heatmap,
                                            scales={'row': y_heatmap_scale, 'column':x_heatmap_scale, 'color': colour_scale},
                                            interactions={'click':'select'},
                      selected_style={'opacity': '1.0'}, unselected_style={'opacity': '0.4'})

    heatmap =bqp.Figure(marks=[heatmap_marks,heatmap_tile_labels],axes=[x_heatmap_axis,y_heatmap_axis,color_axis],
                                background_style={'fill':'white'},
                                padding_x=0.025,
                                padding_y=0,
                                layout=ipw.Layout(width='1000px'))
    return heatmap 