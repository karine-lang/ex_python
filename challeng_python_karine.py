
# Temos duas listas, que são : 



lista1 = ['shipment_number','plant','postal_code_plant','street_plant','house_number_plant','city_plant','delivery','shiptoparty','name_1shipto','zip_codeshipto','city_shipto','street_shipto','carrier_name','additional_data_2',
'goods_movement_date','lane_type','delivery_date','weight_of_delivery_tones','hectolitre_volume_shpmt','transport_info','pallet_quantity','pallet_spot','lh','fsc','heat','stop_charge','other_ass','spot_rate','total',
'shipment_distance_in_km','transportation_planning_point','overall_transportation_status','carrier','shipping_point','shipping_point_desc','reference_doc','reference_doc_item','reference_doc_type','shipment_completion_date',
'planned_date_of_checkin','planned_time_of_checkin','additional_data_1','dlv_type_desc','ref_doc_type_desc','sto_scheduled_quantity','sto_gr_quantity','sto_gi_quantity','goods_receipt_date','pallet_qty_gi','delay_reason',
'material_number','material_desc','qty_deliveredin_base_uom','base_uom','storage_location','volume_of_delivery_in_hectoliters','material_type','shipment_created_on','shipment_changed_on','pricing_procedure',
'shipping_instructions_sto','po_transportation_service','inventory_type']

lista2 = ['shipment_number','plant','postal_code_plant','street_plant','house_number_plant','city_plant','delivery','shiptoparty','name_1ship_to','zip_codeship_to','city_ship_to','street_ship_to','carrier_name','additional_data_2',
 'goods_movement_date','lane_type','delivery_date','weight_of_delivery_tones','hectolitre_volume_shpmt','transport_info','pallet_quantity','pallet_spot','ih','fsc','heat','stop_charge','spot_rate','total',
'shipment_distance_in_km','transportation_planning_point','overall_transportation_status','shipping_point','shipping_point_desc','reference_doc','reference_doc_item','reference_doc_type','shipment_completion_date',
 'planned_date_of_check_in','planned_time_of_checkin','additional_data_1','dlv_type_desc','ref_doc_type_desc','sto_scheduled_quantity','sto_gr_quantity','sto_gi_quantity','goods_receipt_date','pallet_qty_gi','delay_reason',
 'material_number','material_desc','qty_deliveredin_base_uom','base_uom','storage_location','volume_of_delivery_in_hectoliters','material_type','shipment_created_on','shipment_changed_on','pricing_procedure',
 'shipping_instructions_sto','po_transportation_service','inventory_type']
new_list_append = []




#Utilizando conceitos como for loop e list comprehension, compare os elementos entre as duas listas e traga os elementos que são diferentes.

for item in lista1 : 
   if item not in lista2 : 
       new_list_append.append(item) 
        
print(new_list_append)  

 


#Faça utilizando um for loop normal e também utilizando o conceito de list comprehension

new_list_comprehension = [item for item in lista1 if item not in lista2]
print(new_list_comprehension)


# jeito alternativo que eu encontrei pesquisando e achei legal 
defe = set(lista1).difference(set(lista2)) 
print(defe)