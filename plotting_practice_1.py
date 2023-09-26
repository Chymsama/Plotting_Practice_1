#!/usr/bin/env python
# coding: utf-8

# # Bài 11: Practice 1

# In[15]:


import numpy as np
import pandas as pd
import re

import matplotlib.pyplot as plt
import seaborn as sns


# ### 1. Load data
# - Load file `superstore_sales.xlsx` vào biến `df`

# In[16]:


data_path ="D:\codegym3\\" 
data_name= "superstore_sales.xlsx"

order_sh = 'Orders'
returns_sh = 'Returns'
people_sh = 'People'


# In[17]:


order_df = pd.read_excel(data_path+data_name, sheet_name=order_sh)
order_df.head(3)


# In[18]:


returns_df = pd.read_excel(data_path+data_name, sheet_name=returns_sh)
returns_df.head(3)


# In[19]:


people_df = pd.read_excel(data_path+data_name, sheet_name=people_sh)
people_df.head(3)


# ### 2. Inspect data

# - Show 3 dòng đầu

# In[20]:


order_df.head(3)


# In[21]:


returns_df.head(3)


# In[22]:


people_df.head(3)


# - Show 3 dòng cuối

# In[23]:


order_df.tail(3)


# In[24]:


returns_df.tail(3)


# In[25]:


people_df.tail(3)


# - Data có bao nhiêu dòng, bao nhiêu cột?

# In[26]:


order_df.shape


# In[27]:


returns_df.shape


# In[28]:


people_df.shape


# - In ra list tên các cột

# In[29]:


order_df.columns.tolist()


# In[30]:


returns_df.columns.tolist()


# In[31]:


people_df.columns.tolist()


# - Kiểu dữ liệu của từng cột

# In[32]:


order_df.dtypes


# In[33]:


returns_df.dtypes


# In[34]:


people_df.dtypes


# ### 3. Transform cột
# 

# #### 3.1. Đổi tên cột

# - Biến tên cột về dạng chữ thường và snake_case

# In[35]:


def covert_name(text):
    text =text.lower()
    text = text.replace(' ','_')
    return text

order_df.columns = order_df.columns.map(covert_name)

order_df.head(3)


# In[36]:


people_df.columns = people_df.columns.map(covert_name)
people_df.head(3)


# In[37]:


returns_df.columns = returns_df.columns.map(covert_name)
returns_df.head(3)


# - In ra 1 dòng đầu để kiểm tra

# In[ ]:





# #### 3.2. Đổi về datetime

# - Chọn ra cột mà tên có chứa `date` và kiểm tra dtype của chúng

# In[38]:


date_colums = order_df.filter(like = 'date')

for col in date_colums.columns:
    dtypes = date_colums[col].dtype
    print (f"Cột '{col}' có kiểu dữ liệu : {dtypes}")


# - Nếu chưa ở dạng datetime thì đổi thành datetime. Nếu đã ở dạng datetime thì vẫn cứ đổi lại để practice.

# pd.to_datetime nha thầy, e hơi lười hehehe

# - Kiểm tra kết quả sau khi đổi

# In[ ]:





# ### 4. Trả lời các câu hỏi khác

# #### 4.1. Distinct values

# - Có bao nhiêu nước và là những nước nào?

# In[39]:


count_countries = order_df['country'].unique()
num_countries = len(count_countries)

print ("Số lượng quốc gia là ",num_countries)
print ("Những nước đó là ", count_countries)


# In[ ]:





# - Có bao nhiêu categories và là những categories nào?

# In[40]:


count_categories = order_df['category'].unique()
num_categories = len(count_categories)

print ("Số lượng categori là ", num_categories)
print("Những categories đó là ", count_categories)


# - Có bao nhiêu subcategories và là những subcategories nào?

# In[41]:


count_subcate = order_df['sub-category'].unique()
num_subcate = len(count_subcate)

print ("Số lượng subcategori là ", num_subcate)
print("Những subcategories đó là ", count_subcate)


# In[ ]:





# - Tương tự có bao nhiêu `city`, `region`, `state`, `ship_mode`, `segment` (gợi ý dùng `for`)

# In[42]:


columns_to_count = ['city', 'region', 'state', 'ship_mode', 'segment']


for col in columns_to_count:
    unique_values = order_df[col].unique()
    num_unique = len(unique_values)
    
    print(f"Có {num_unique} {col} và là:")
    for value in unique_values:
        print(value)
    print()


# #### 4.2. Làm việc với ngày tháng

# - Data chứa các order trong khoảng thời gian nào?

# In[43]:


star_date = order_df['order_date'].min()
end_date = order_df['order_date'].max()

print("data chứa order từ",star_date,"đến", end_date)


# - Mỗi năm có bao nhiêu order (sắp xếp theo thứ tự các năm tăng dần)?

# In[44]:


order_count_by_year = order_df.groupby(order_df['order_date'].dt.year)['order_date'].size().reset_index(name='Order Count')


# In[45]:


order_count_by_year = order_count_by_year.sort_values('order_date')

print(order_count_by_year)



# - Vẽ đồ thị cho thống kê trên

# In[46]:


plt.figure(figsize=(10, 6))
plt.bar(order_count_by_year['order_date'], order_count_by_year['Order Count'], color='skyblue')
plt.xlabel('Năm')
plt.ylabel('Số Đơn Đặt Hàng')
plt.title('Số Đơn Đặt Hàng Theo Năm')
plt.xticks(order_count_by_year['order_date'])
plt.show()


# - Mỗi tháng có bao nhiêu order?

# In[47]:


order_count_by_month = order_df.groupby(order_df['order_date'].dt.month)['order_date'].size().reset_index(name='Order Count')


# In[48]:


order_count_by_month = order_count_by_month.sort_values('order_date')
print(order_count_by_month)


# - Vẽ plot cho data trên (bar, line)

# In[49]:


plt.figure(figsize=(10, 6))
plt.bar(order_count_by_month['order_date'], order_count_by_month['Order Count'], color='skyblue')
plt.xlabel('Tháng')
plt.ylabel('Số Đơn Đặt Hàng')
plt.title('Số Đơn Đặt Hàng Theo Tháng')
plt.xticks(order_count_by_month['order_date'])
plt.show()


# In[50]:


plt.figure(figsize=(10, 6))
plt.plot(order_count_by_month['order_date'], order_count_by_month['Order Count'], marker='o', color='green', linestyle='-')
plt.xlabel('Tháng')
plt.ylabel('Số Đơn Đặt Hàng')
plt.title('Số Đơn Đặt Hàng Theo Tháng')
plt.xticks(order_count_by_month['order_date'])
plt.grid(True)
plt.show()


# In[ ]:





# - Vẽ barplot như trên nhưng alternate màu của 2 năm liên tiếp

# In[51]:


order_count_by_year.head()


# In[52]:


colors = ['skyblue' if i % 2 == 0 else 'lightcoral' for i in range(len(order_count_by_year))]


# In[53]:


plt.figure(figsize=(10, 6))
plt.bar(order_count_by_year['order_date'], order_count_by_year['Order Count'], color=colors)
plt.xlabel('Tháng')
plt.ylabel('Số Đơn Đặt Hàng')
plt.title('Số Đơn Đặt Hàng Theo Tháng (Màu Xen Kẽ)')
plt.xticks(order_count_by_year['order_date'])
plt.show()


# In[ ]:





# - Như yêu cầu trên nhưng vẽ line plot (gợi ý, dùng `sns.pointplot`)

# In[54]:


palette = sns.color_palette(["skyblue", "lightcoral"])

plt.figure(figsize=(10, 6))
sns.pointplot(x='order_date', y='Order Count', data=order_count_by_month, hue=order_count_by_month['order_date'] % 2, palette=palette)
plt.xlabel('Tháng')
plt.ylabel('Số Đơn Đặt Hàng')
plt.title('Số Đơn Đặt Hàng Theo Tháng (Line Plot với Màu Xen Kẽ)')
plt.xticks(order_count_by_month['order_date'])
plt.legend(title='Năm', labels=['Chẵn', 'Lẻ'])
plt.show()


# ### 4.3. Doanh thu

# - Lấy ra các đơn hàng của năm 2017

# In[111]:


orders_2017 = order_df[order_df['order_date'].dt.year == 2017]

orders_2017.head()


# - Có bao nhiêu đơn hàng?

# In[115]:


orders_2017.shape[0]


# - Số đơn hàng mỗi tháng?

# In[116]:


orders_2017_copy = orders_2017.rename(columns={'order_date': 'order_date_datetime'})

order_count_by_month_2017 = orders_2017_copy.groupby(orders_2017_copy['order_date_datetime'].dt.month)['order_date_datetime'].count().reset_index()
order_count_by_month_2017.columns = ['Tháng', 'Số Đơn Hàng 2017']

print(order_count_by_month_2017)

df_temp = orders_2017.copy()
df_temp.rename(columns={'order_date': 'order_date_datetime'}, inplace=True)

order_count_by_month_2017 = df_temp.groupby(df_temp['order_date_datetime'].dt.month)['order_date_datetime'].count().reset_index()
order_count_by_month_2017.columns = ['Tháng', 'Số Đơn Hàng 2017']

print(order_count_by_month_2017)


# e không hiểu sao nó lại lỗi như rứa trong khi e không insert cột nào , e chỉ dùng cột đó để group by :(((

# - Lấy ra top 10 sản phẩm có doanh số cao nhất 2017

# In[124]:


top_products_2017 = orders_2017.groupby(['product_name','category'])['sales'].sum().reset_index()

top_products_2017 = top_products_2017.sort_values(by='sales', ascending=False)

top_10_products_2017 = top_products_2017.head(10)

print(top_10_products_2017)


# - Lấy ra top 10 như trên nhưng tô màu theo category

# In[125]:


plt.figure(figsize=(12, 6))
sns.barplot(x='sales', y='product_name', hue='category', data=top_10_products_2017)
plt.title('Top 10 Sản phẩm có doanh số cao nhất năm 2017 (Tô màu theo Category)')
plt.xlabel('Doanh số')
plt.ylabel('Sản phẩm')
plt.legend(title='Category', loc='upper right')
plt.show()


# - Lọc ra top 5 sub-categories có Sales nhiều nhất trong năm 2017

# In[126]:


top_subcategories_2017 = orders_2017.groupby('sub-category')['sales'].sum().reset_index()


# In[129]:


top_subcategories_2017 = top_subcategories_2017.sort_values(by='sales', ascending=False)


# In[136]:


top_5_subcategories_2017 = top_subcategories_2017.head(5)

top_5_subcategories_2017.head()


# - Vẽ barplot cho sales của 5 sub-categories theo từng năm từ năm 2014-2017

# In[149]:


sales_by_year_subcategory = order_df.groupby([order_df['order_date'].dt.year, 'sub-category'])['sales'].sum().reset_index()


# In[150]:


top_5_subcategories = sales_by_year_subcategory.groupby('sub-category')['sales'].sum().nlargest(5).index


# In[151]:


sales_by_year_top_5 = sales_by_year_subcategory[sales_by_year_subcategory['sub-category'].isin(top_5_subcategories)]


# In[152]:


plt.figure(figsize=(12, 6))
sns.barplot(x='order_date', y='sales', hue='sub-category', data=sales_by_year_top_5)
plt.title('Doanh số của 5 Sub-Categories theo từng năm (2014-2017)')
plt.xlabel('Năm')
plt.ylabel('Doanh số')
plt.legend(title='Sub-Category')
plt.show()


# - Vẽ boxplot của doanh số daily từng category theo các năm

# In[168]:


daily_sales_by_category = order_df[['order_date', 'category', 'sales']].copy()

daily_sales_by_category['year'] = daily_sales_by_category['order_date'].dt.year


# In[165]:


plt.figure(figsize=(12, 6))
sns.boxplot(x='year', y='sales', hue='category', data=daily_sales_by_category)
plt.title('Boxplot của Doanh số hàng ngày theo Category (2014-2017)')
plt.xlabel('Năm')
plt.ylabel('Doanh số')
plt.xticks(rotation=45)
plt.legend(title='Category')
plt.show()


# - Vẽ KDE của doanh số daily từng category theo các năm

# In[169]:


plt.figure(figsize=(12, 6))
sns.kdeplot(data=daily_sales_by_category, x='sales', hue='category', common_norm=False)
plt.title('KDE của Doanh số hàng ngày theo Category (2014-2017)')
plt.xlabel('Doanh số')
plt.ylabel('Mật độ')
plt.legend(title='Category')
plt.show()


# - Vẽ daily sales against daily quantity

# In[170]:


daily_sales_quantity = order_df[['order_date', 'sales', 'quantity']].copy()


# In[171]:


plt.figure(figsize=(12, 6))
plt.scatter(daily_sales_quantity['quantity'], daily_sales_quantity['sales'], alpha=0.5)
plt.title('Daily Sales vs. Daily Quantity')
plt.xlabel('Daily Quantity')
plt.ylabel('Daily Sales')
plt.grid(True)
plt.show()


# - Vẽ daily sales against daily quantity (từ category ra riêng từng subplots)

# In[172]:


daily_sales_quantity_category = order_df[['order_date', 'category', 'sales', 'quantity']].copy()


# In[173]:


categories = daily_sales_quantity_category['category'].unique()


# In[176]:


fig, axes = plt.subplots(nrows=len(categories), figsize=(12, 6 * len(categories)))
for i, category in enumerate(categories):
    data_category = daily_sales_quantity_category[daily_sales_quantity_category['category'] == category]
    ax = axes[i]
    ax.scatter(data_category['quantity'], data_category['sales'], alpha=0.5)
    ax.set_title(f'Daily Sales vs. Daily Quantity ({category})')
    ax.set_xlabel('Daily Quantity')
    ax.set_ylabel('Daily Sales')
    ax.grid(True)

plt.tight_layout()


plt.show()


# In[ ]:





# - Lọc ra các đơn hàng bị chuyển chậm hơn 3 ngày

# In[198]:


order_df['shipping_duration'] = (order_df['ship_date'] - order_df['order_date']).dt.days


# In[200]:


slow_shipments = order_df[order_df['shipping_duration'] >= 3]

slow_shipments.head()


# - Có bao nhiêu đơn như vậy

# In[201]:


slow_shipments.shape[0]


# - Đơn hàng trễ nhất là bao lâu?

# In[208]:


slow_shipments_sorted = slow_shipments.sort_values(by='shipping_duration', ascending=False)
slowest_shipment = slow_shipments_sorted.iloc[0]
print("Thông tin về đơn hàng trễ nhất:")
print(slowest_shipment)

slowest_duration = slowest_shipment['shipping_duration']
print(f"Đơn hàng trễ nhất đã bị chuyển chậm {slowest_duration} ngày.")


# - Vẽ boxplot thời gian chờ cho từng `region`

# In[209]:


plt.figure(figsize=(12, 6))
sns.boxplot(x='region', y='shipping_duration', data=order_df)
plt.title('Boxplot Thời gian chờ theo Region')
plt.xlabel('Region')
plt.ylabel('Thời gian chờ (ngày)')
plt.xticks(rotation=45)
plt.show()


# - Vẽ boxplot thời gian chờ cho từng `ship_mode`

# In[210]:


plt.figure(figsize=(12, 6))
sns.boxplot(x='ship_mode', y='shipping_duration', data=order_df)
plt.title('Boxplot Thời gian chờ theo Ship Mode')
plt.xlabel('Ship Mode')
plt.ylabel('Thời gian chờ (ngày)')
plt.xticks(rotation=45)
plt.show()


# - Điều chỉnh lại subplots trên sao cho box xếp theo thứ tự `Same day`, `First Class`, `Second Class`, `Standard Class`

# In[213]:


ship_mode_order = ["Same day", "First Class", "Second Class", "Standard Class"]


# In[214]:


plt.figure(figsize=(12, 6))
sns.boxplot(x='ship_mode', y='shipping_duration', data=order_df, order=ship_mode_order)
plt.title('Boxplot Thời gian chờ theo Ship Mode')
plt.xlabel('Ship Mode')
plt.ylabel('Thời gian chờ (ngày)')
plt.xticks(rotation=45)
plt.show()

