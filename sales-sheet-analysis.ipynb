{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "papermill": {
     "duration": 0.016611,
     "end_time": "2021-04-09T07:39:23.919343",
     "exception": false,
     "start_time": "2021-04-09T07:39:23.902732",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# The questions:\n",
    "\n",
    "* **What's the sales trend?**\n",
    "* **What's the most preferred shipment method?**\n",
    "* **What's profitability of each category?**\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "papermill": {
     "duration": 0.015608,
     "end_time": "2021-04-09T07:39:23.950991",
     "exception": false,
     "start_time": "2021-04-09T07:39:23.935383",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "___"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "papermill": {
     "duration": 0.015592,
     "end_time": "2021-04-09T07:39:23.982730",
     "exception": false,
     "start_time": "2021-04-09T07:39:23.967138",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "## Installing/importing needed libraries:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2021-04-09T07:39:24.018715Z",
     "iopub.status.busy": "2021-04-09T07:39:24.018154Z",
     "iopub.status.idle": "2021-04-09T07:39:33.692683Z",
     "shell.execute_reply": "2021-04-09T07:39:33.691902Z"
    },
    "papermill": {
     "duration": 9.694637,
     "end_time": "2021-04-09T07:39:33.692899",
     "exception": false,
     "start_time": "2021-04-09T07:39:23.998262",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting openpyxl\r\n",
      "  Downloading openpyxl-3.0.7-py2.py3-none-any.whl (243 kB)\r\n",
      "\u001b[K     |████████████████████████████████| 243 kB 1.3 MB/s \r\n",
      "\u001b[?25hCollecting et-xmlfile\r\n",
      "  Downloading et_xmlfile-1.0.1.tar.gz (8.4 kB)\r\n",
      "Building wheels for collected packages: et-xmlfile\r\n",
      "  Building wheel for et-xmlfile (setup.py) ... \u001b[?25l-\b \b\\\b \bdone\r\n",
      "\u001b[?25h  Created wheel for et-xmlfile: filename=et_xmlfile-1.0.1-py3-none-any.whl size=8913 sha256=ac57a3cd946229683432fb36b5a8eed89f47744558e8734749fe9d36920af4e1\r\n",
      "  Stored in directory: /root/.cache/pip/wheels/e2/bd/55/048b4fd505716c4c298f42ee02dffd9496bb6d212b266c7f31\r\n",
      "Successfully built et-xmlfile\r\n",
      "Installing collected packages: et-xmlfile, openpyxl\r\n",
      "Successfully installed et-xmlfile-1.0.1 openpyxl-3.0.7\r\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install openpyxl"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2021-04-09T07:39:33.740031Z",
     "iopub.status.busy": "2021-04-09T07:39:33.739240Z",
     "iopub.status.idle": "2021-04-09T07:39:34.428387Z",
     "shell.execute_reply": "2021-04-09T07:39:34.427902Z"
    },
    "papermill": {
     "duration": 0.714953,
     "end_time": "2021-04-09T07:39:34.428519",
     "exception": false,
     "start_time": "2021-04-09T07:39:33.713566",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "\n",
    "%matplotlib inline"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "papermill": {
     "duration": 0.019657,
     "end_time": "2021-04-09T07:39:34.468645",
     "exception": false,
     "start_time": "2021-04-09T07:39:34.448988",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "## Importing the sheets we will work on: "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2021-04-09T07:39:34.513096Z",
     "iopub.status.busy": "2021-04-09T07:39:34.512243Z",
     "iopub.status.idle": "2021-04-09T07:39:55.779669Z",
     "shell.execute_reply": "2021-04-09T07:39:55.779082Z"
    },
    "papermill": {
     "duration": 21.291329,
     "end_time": "2021-04-09T07:39:55.779796",
     "exception": false,
     "start_time": "2021-04-09T07:39:34.488467",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>order_id</th>\n",
       "      <th>order_date</th>\n",
       "      <th>ship_date</th>\n",
       "      <th>ship_mode</th>\n",
       "      <th>customer_name</th>\n",
       "      <th>segment</th>\n",
       "      <th>state</th>\n",
       "      <th>country</th>\n",
       "      <th>market</th>\n",
       "      <th>region</th>\n",
       "      <th>...</th>\n",
       "      <th>category</th>\n",
       "      <th>sub_category</th>\n",
       "      <th>product_name</th>\n",
       "      <th>sales</th>\n",
       "      <th>quantity</th>\n",
       "      <th>discount</th>\n",
       "      <th>profit</th>\n",
       "      <th>shipping_cost</th>\n",
       "      <th>order_priority</th>\n",
       "      <th>year</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>AG-2011-2040</td>\n",
       "      <td>2011-01-01</td>\n",
       "      <td>2011-01-06</td>\n",
       "      <td>Standard Class</td>\n",
       "      <td>Toby Braunhardt</td>\n",
       "      <td>Consumer</td>\n",
       "      <td>Constantine</td>\n",
       "      <td>Algeria</td>\n",
       "      <td>Africa</td>\n",
       "      <td>Africa</td>\n",
       "      <td>...</td>\n",
       "      <td>Office Supplies</td>\n",
       "      <td>Storage</td>\n",
       "      <td>Tenex Lockers, Blue</td>\n",
       "      <td>408.300</td>\n",
       "      <td>2</td>\n",
       "      <td>0.0</td>\n",
       "      <td>106.140</td>\n",
       "      <td>35.46</td>\n",
       "      <td>Medium</td>\n",
       "      <td>2011</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>IN-2011-47883</td>\n",
       "      <td>2011-01-01</td>\n",
       "      <td>2011-01-08</td>\n",
       "      <td>Standard Class</td>\n",
       "      <td>Joseph Holt</td>\n",
       "      <td>Consumer</td>\n",
       "      <td>New South Wales</td>\n",
       "      <td>Australia</td>\n",
       "      <td>APAC</td>\n",
       "      <td>Oceania</td>\n",
       "      <td>...</td>\n",
       "      <td>Office Supplies</td>\n",
       "      <td>Supplies</td>\n",
       "      <td>Acme Trimmer, High Speed</td>\n",
       "      <td>120.366</td>\n",
       "      <td>3</td>\n",
       "      <td>0.1</td>\n",
       "      <td>36.036</td>\n",
       "      <td>9.72</td>\n",
       "      <td>Medium</td>\n",
       "      <td>2011</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>2 rows × 21 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "        order_id order_date  ship_date       ship_mode    customer_name  \\\n",
       "0   AG-2011-2040 2011-01-01 2011-01-06  Standard Class  Toby Braunhardt   \n",
       "1  IN-2011-47883 2011-01-01 2011-01-08  Standard Class      Joseph Holt   \n",
       "\n",
       "    segment            state    country  market   region  ...  \\\n",
       "0  Consumer      Constantine    Algeria  Africa   Africa  ...   \n",
       "1  Consumer  New South Wales  Australia    APAC  Oceania  ...   \n",
       "\n",
       "          category sub_category              product_name    sales  quantity  \\\n",
       "0  Office Supplies      Storage       Tenex Lockers, Blue  408.300         2   \n",
       "1  Office Supplies     Supplies  Acme Trimmer, High Speed  120.366         3   \n",
       "\n",
       "   discount   profit  shipping_cost  order_priority  year  \n",
       "0       0.0  106.140          35.46          Medium  2011  \n",
       "1       0.1   36.036           9.72          Medium  2011  \n",
       "\n",
       "[2 rows x 21 columns]"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "orders = pd.read_excel('../input/sales-sheet/superstore_sales.xlsx', sheet_name='Orders', engine='openpyxl')\n",
    "orders.head(2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2021-04-09T07:39:55.828149Z",
     "iopub.status.busy": "2021-04-09T07:39:55.827631Z",
     "iopub.status.idle": "2021-04-09T07:39:56.720886Z",
     "shell.execute_reply": "2021-04-09T07:39:56.721642Z"
    },
    "papermill": {
     "duration": 0.918089,
     "end_time": "2021-04-09T07:39:56.721810",
     "exception": false,
     "start_time": "2021-04-09T07:39:55.803721",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Person</th>\n",
       "      <th>Region</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Anna Andreadi</td>\n",
       "      <td>Central</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Chuck Magee</td>\n",
       "      <td>South</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Kelly Williams</td>\n",
       "      <td>East</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Matt Collister</td>\n",
       "      <td>West</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Deborah Brumfield</td>\n",
       "      <td>Africa</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Larry Hughes</td>\n",
       "      <td>AMEA</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Nicole Hansen</td>\n",
       "      <td>Canada</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>Giulietta Dortch</td>\n",
       "      <td>Caribbean</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Nora Preis</td>\n",
       "      <td>Central Asia</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>Jack Lebron</td>\n",
       "      <td>North</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>Shirley Daniels</td>\n",
       "      <td>North Asia</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>Anthony Jacobs</td>\n",
       "      <td>Oceania</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>Alejandro Ballentine</td>\n",
       "      <td>Southeast Asia</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>Abcd</td>\n",
       "      <td>India</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                  Person          Region\n",
       "0          Anna Andreadi         Central\n",
       "1            Chuck Magee           South\n",
       "2         Kelly Williams            East\n",
       "3         Matt Collister            West\n",
       "4      Deborah Brumfield          Africa\n",
       "5           Larry Hughes            AMEA\n",
       "6          Nicole Hansen          Canada\n",
       "7       Giulietta Dortch       Caribbean\n",
       "8             Nora Preis    Central Asia\n",
       "9            Jack Lebron           North\n",
       "10       Shirley Daniels      North Asia\n",
       "11        Anthony Jacobs         Oceania\n",
       "12  Alejandro Ballentine  Southeast Asia\n",
       "13                  Abcd           India"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "people = pd.read_excel('../input/sales-sheet/superstore_sales.xlsx', sheet_name='People', engine='openpyxl')\n",
    "people"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2021-04-09T07:39:56.769765Z",
     "iopub.status.busy": "2021-04-09T07:39:56.768975Z",
     "iopub.status.idle": "2021-04-09T07:39:57.673974Z",
     "shell.execute_reply": "2021-04-09T07:39:57.674392Z"
    },
    "papermill": {
     "duration": 0.931832,
     "end_time": "2021-04-09T07:39:57.674535",
     "exception": false,
     "start_time": "2021-04-09T07:39:56.742703",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Returned</th>\n",
       "      <th>Order ID</th>\n",
       "      <th>Market</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Yes</td>\n",
       "      <td>MX-2013-168137</td>\n",
       "      <td>LATAM</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Yes</td>\n",
       "      <td>US-2011-165316</td>\n",
       "      <td>LATAM</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Yes</td>\n",
       "      <td>ES-2013-1525878</td>\n",
       "      <td>EU</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Yes</td>\n",
       "      <td>CA-2013-118311</td>\n",
       "      <td>United States</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Yes</td>\n",
       "      <td>ES-2011-1276768</td>\n",
       "      <td>EU</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Yes</td>\n",
       "      <td>MX-2013-131247</td>\n",
       "      <td>LATAM</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Yes</td>\n",
       "      <td>ID-2011-20975</td>\n",
       "      <td>APAC</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>Yes</td>\n",
       "      <td>IN-2014-58460</td>\n",
       "      <td>APAC</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Yes</td>\n",
       "      <td>ES-2011-3028321</td>\n",
       "      <td>EU</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>Yes</td>\n",
       "      <td>MX-2014-148285</td>\n",
       "      <td>LATAM</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Returned         Order ID         Market\n",
       "0      Yes   MX-2013-168137          LATAM\n",
       "1      Yes   US-2011-165316          LATAM\n",
       "2      Yes  ES-2013-1525878             EU\n",
       "3      Yes   CA-2013-118311  United States\n",
       "4      Yes  ES-2011-1276768             EU\n",
       "5      Yes   MX-2013-131247          LATAM\n",
       "6      Yes    ID-2011-20975           APAC\n",
       "7      Yes    IN-2014-58460           APAC\n",
       "8      Yes  ES-2011-3028321             EU\n",
       "9      Yes   MX-2014-148285          LATAM"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "returns = pd.read_excel('../input/sales-sheet/superstore_sales.xlsx', sheet_name='Returns', engine='openpyxl')\n",
    "returns.head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2021-04-09T07:39:57.725538Z",
     "iopub.status.busy": "2021-04-09T07:39:57.724767Z",
     "iopub.status.idle": "2021-04-09T07:39:57.857513Z",
     "shell.execute_reply": "2021-04-09T07:39:57.857903Z"
    },
    "papermill": {
     "duration": 0.162007,
     "end_time": "2021-04-09T07:39:57.858038",
     "exception": false,
     "start_time": "2021-04-09T07:39:57.696031",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "In the returns sheet, there're: \n",
      " LATAM            297\n",
      "APAC             296\n",
      "United States    296\n",
      "EU               284\n",
      "Name: Market, dtype: int64\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/opt/conda/lib/python3.7/site-packages/seaborn/_decorators.py:43: FutureWarning: Pass the following variable as a keyword arg: x. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.\n",
      "  FutureWarning\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "print('In the returns sheet, there\\'re: \\n', returns.Market.value_counts())\n",
    "sns.countplot(returns['Market'])\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2021-04-09T07:39:57.907397Z",
     "iopub.status.busy": "2021-04-09T07:39:57.906740Z",
     "iopub.status.idle": "2021-04-09T07:39:57.976116Z",
     "shell.execute_reply": "2021-04-09T07:39:57.975502Z"
    },
    "papermill": {
     "duration": 0.095743,
     "end_time": "2021-04-09T07:39:57.976270",
     "exception": false,
     "start_time": "2021-04-09T07:39:57.880527",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 51290 entries, 0 to 51289\n",
      "Data columns (total 21 columns):\n",
      " #   Column          Non-Null Count  Dtype         \n",
      "---  ------          --------------  -----         \n",
      " 0   order_id        51290 non-null  object        \n",
      " 1   order_date      51290 non-null  datetime64[ns]\n",
      " 2   ship_date       51290 non-null  datetime64[ns]\n",
      " 3   ship_mode       51290 non-null  object        \n",
      " 4   customer_name   51290 non-null  object        \n",
      " 5   segment         51290 non-null  object        \n",
      " 6   state           51290 non-null  object        \n",
      " 7   country         51290 non-null  object        \n",
      " 8   market          51290 non-null  object        \n",
      " 9   region          51290 non-null  object        \n",
      " 10  product_id      51290 non-null  object        \n",
      " 11  category        51290 non-null  object        \n",
      " 12  sub_category    51290 non-null  object        \n",
      " 13  product_name    51290 non-null  object        \n",
      " 14  sales           51290 non-null  float64       \n",
      " 15  quantity        51290 non-null  int64         \n",
      " 16  discount        51290 non-null  float64       \n",
      " 17  profit          51290 non-null  float64       \n",
      " 18  shipping_cost   51290 non-null  float64       \n",
      " 19  order_priority  51290 non-null  object        \n",
      " 20  year            51290 non-null  int64         \n",
      "dtypes: datetime64[ns](2), float64(4), int64(2), object(13)\n",
      "memory usage: 8.2+ MB\n"
     ]
    }
   ],
   "source": [
    "orders.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2021-04-09T07:39:58.027683Z",
     "iopub.status.busy": "2021-04-09T07:39:58.026828Z",
     "iopub.status.idle": "2021-04-09T07:39:58.030122Z",
     "shell.execute_reply": "2021-04-09T07:39:58.030614Z"
    },
    "papermill": {
     "duration": 0.030847,
     "end_time": "2021-04-09T07:39:58.030741",
     "exception": false,
     "start_time": "2021-04-09T07:39:57.999894",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['order_id', 'order_date', 'ship_date', 'ship_mode', 'customer_name',\n",
       "       'segment', 'state', 'country', 'market', 'region', 'product_id',\n",
       "       'category', 'sub_category', 'product_name', 'sales', 'quantity',\n",
       "       'discount', 'profit', 'shipping_cost', 'order_priority', 'year'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "orders.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2021-04-09T07:39:58.082001Z",
     "iopub.status.busy": "2021-04-09T07:39:58.081226Z",
     "iopub.status.idle": "2021-04-09T07:39:58.087438Z",
     "shell.execute_reply": "2021-04-09T07:39:58.087942Z"
    },
    "papermill": {
     "duration": 0.033929,
     "end_time": "2021-04-09T07:39:58.088057",
     "exception": false,
     "start_time": "2021-04-09T07:39:58.054128",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "data = orders[['order_id', 'order_date', 'ship_date', 'ship_mode', 'product_id',\n",
    "       'category', 'sub_category', 'product_name', 'sales', 'quantity',\n",
    "       'profit']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2021-04-09T07:39:58.138752Z",
     "iopub.status.busy": "2021-04-09T07:39:58.138130Z",
     "iopub.status.idle": "2021-04-09T07:39:58.140911Z",
     "shell.execute_reply": "2021-04-09T07:39:58.140455Z"
    },
    "papermill": {
     "duration": 0.029395,
     "end_time": "2021-04-09T07:39:58.141017",
     "exception": false,
     "start_time": "2021-04-09T07:39:58.111622",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "data.index = np.arange(1, len(data) +1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2021-04-09T07:39:58.192981Z",
     "iopub.status.busy": "2021-04-09T07:39:58.192193Z",
     "iopub.status.idle": "2021-04-09T07:39:58.204048Z",
     "shell.execute_reply": "2021-04-09T07:39:58.204480Z"
    },
    "papermill": {
     "duration": 0.03997,
     "end_time": "2021-04-09T07:39:58.204608",
     "exception": false,
     "start_time": "2021-04-09T07:39:58.164638",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>order_id</th>\n",
       "      <th>order_date</th>\n",
       "      <th>ship_date</th>\n",
       "      <th>ship_mode</th>\n",
       "      <th>product_id</th>\n",
       "      <th>category</th>\n",
       "      <th>sub_category</th>\n",
       "      <th>product_name</th>\n",
       "      <th>sales</th>\n",
       "      <th>quantity</th>\n",
       "      <th>profit</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>AG-2011-2040</td>\n",
       "      <td>2011-01-01</td>\n",
       "      <td>2011-01-06</td>\n",
       "      <td>Standard Class</td>\n",
       "      <td>OFF-TEN-10000025</td>\n",
       "      <td>Office Supplies</td>\n",
       "      <td>Storage</td>\n",
       "      <td>Tenex Lockers, Blue</td>\n",
       "      <td>408.300</td>\n",
       "      <td>2</td>\n",
       "      <td>106.140</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>IN-2011-47883</td>\n",
       "      <td>2011-01-01</td>\n",
       "      <td>2011-01-08</td>\n",
       "      <td>Standard Class</td>\n",
       "      <td>OFF-SU-10000618</td>\n",
       "      <td>Office Supplies</td>\n",
       "      <td>Supplies</td>\n",
       "      <td>Acme Trimmer, High Speed</td>\n",
       "      <td>120.366</td>\n",
       "      <td>3</td>\n",
       "      <td>36.036</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        order_id order_date  ship_date       ship_mode        product_id  \\\n",
       "1   AG-2011-2040 2011-01-01 2011-01-06  Standard Class  OFF-TEN-10000025   \n",
       "2  IN-2011-47883 2011-01-01 2011-01-08  Standard Class   OFF-SU-10000618   \n",
       "\n",
       "          category sub_category              product_name    sales  quantity  \\\n",
       "1  Office Supplies      Storage       Tenex Lockers, Blue  408.300         2   \n",
       "2  Office Supplies     Supplies  Acme Trimmer, High Speed  120.366         3   \n",
       "\n",
       "    profit  \n",
       "1  106.140  \n",
       "2   36.036  "
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[:2]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "papermill": {
     "duration": 0.023668,
     "end_time": "2021-04-09T07:39:58.252097",
     "exception": false,
     "start_time": "2021-04-09T07:39:58.228429",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "<h2> What's the sales trend?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2021-04-09T07:39:58.304018Z",
     "iopub.status.busy": "2021-04-09T07:39:58.303209Z",
     "iopub.status.idle": "2021-04-09T07:39:58.309388Z",
     "shell.execute_reply": "2021-04-09T07:39:58.308761Z"
    },
    "papermill": {
     "duration": 0.033469,
     "end_time": "2021-04-09T07:39:58.309523",
     "exception": false,
     "start_time": "2021-04-09T07:39:58.276054",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The first date:\n",
      " 2011-01-01 00:00:00\n",
      "The last date:\n",
      " 2014-12-31 00:00:00\n"
     ]
    }
   ],
   "source": [
    "print('The first date:\\n', data['order_date'].min()) \n",
    "print('The last date:\\n', data['order_date'].max()) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2021-04-09T07:39:58.382448Z",
     "iopub.status.busy": "2021-04-09T07:39:58.377222Z",
     "iopub.status.idle": "2021-04-09T07:39:58.716813Z",
     "shell.execute_reply": "2021-04-09T07:39:58.717540Z"
    },
    "papermill": {
     "duration": 0.383199,
     "end_time": "2021-04-09T07:39:58.717715",
     "exception": false,
     "start_time": "2021-04-09T07:39:58.334516",
     "status": "completed"
    },
    "scrolled": false,
    "tags": []
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/opt/conda/lib/python3.7/site-packages/ipykernel_launcher.py:1: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame.\n",
      "Try using .loc[row_indexer,col_indexer] = value instead\n",
      "\n",
      "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
      "  \"\"\"Entry point for launching an IPython kernel.\n"
     ]
    }
   ],
   "source": [
    "data['month_year'] = data['order_date'].apply(lambda x: x.strftime ('%y-%m'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2021-04-09T07:39:58.783110Z",
     "iopub.status.busy": "2021-04-09T07:39:58.782567Z",
     "iopub.status.idle": "2021-04-09T07:39:58.785905Z",
     "shell.execute_reply": "2021-04-09T07:39:58.786303Z"
    },
    "papermill": {
     "duration": 0.043817,
     "end_time": "2021-04-09T07:39:58.786425",
     "exception": false,
     "start_time": "2021-04-09T07:39:58.742608",
     "status": "completed"
    },
    "scrolled": true,
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>order_id</th>\n",
       "      <th>order_date</th>\n",
       "      <th>ship_date</th>\n",
       "      <th>ship_mode</th>\n",
       "      <th>product_id</th>\n",
       "      <th>category</th>\n",
       "      <th>sub_category</th>\n",
       "      <th>product_name</th>\n",
       "      <th>sales</th>\n",
       "      <th>quantity</th>\n",
       "      <th>profit</th>\n",
       "      <th>month_year</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>AG-2011-2040</td>\n",
       "      <td>2011-01-01</td>\n",
       "      <td>2011-01-06</td>\n",
       "      <td>Standard Class</td>\n",
       "      <td>OFF-TEN-10000025</td>\n",
       "      <td>Office Supplies</td>\n",
       "      <td>Storage</td>\n",
       "      <td>Tenex Lockers, Blue</td>\n",
       "      <td>408.300</td>\n",
       "      <td>2</td>\n",
       "      <td>106.140</td>\n",
       "      <td>11-01</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>IN-2011-47883</td>\n",
       "      <td>2011-01-01</td>\n",
       "      <td>2011-01-08</td>\n",
       "      <td>Standard Class</td>\n",
       "      <td>OFF-SU-10000618</td>\n",
       "      <td>Office Supplies</td>\n",
       "      <td>Supplies</td>\n",
       "      <td>Acme Trimmer, High Speed</td>\n",
       "      <td>120.366</td>\n",
       "      <td>3</td>\n",
       "      <td>36.036</td>\n",
       "      <td>11-01</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>HU-2011-1220</td>\n",
       "      <td>2011-01-01</td>\n",
       "      <td>2011-01-05</td>\n",
       "      <td>Second Class</td>\n",
       "      <td>OFF-TEN-10001585</td>\n",
       "      <td>Office Supplies</td>\n",
       "      <td>Storage</td>\n",
       "      <td>Tenex Box, Single Width</td>\n",
       "      <td>66.120</td>\n",
       "      <td>4</td>\n",
       "      <td>29.640</td>\n",
       "      <td>11-01</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        order_id order_date  ship_date       ship_mode        product_id  \\\n",
       "1   AG-2011-2040 2011-01-01 2011-01-06  Standard Class  OFF-TEN-10000025   \n",
       "2  IN-2011-47883 2011-01-01 2011-01-08  Standard Class   OFF-SU-10000618   \n",
       "3   HU-2011-1220 2011-01-01 2011-01-05    Second Class  OFF-TEN-10001585   \n",
       "\n",
       "          category sub_category              product_name    sales  quantity  \\\n",
       "1  Office Supplies      Storage       Tenex Lockers, Blue  408.300         2   \n",
       "2  Office Supplies     Supplies  Acme Trimmer, High Speed  120.366         3   \n",
       "3  Office Supplies      Storage   Tenex Box, Single Width   66.120         4   \n",
       "\n",
       "    profit month_year  \n",
       "1  106.140      11-01  \n",
       "2   36.036      11-01  \n",
       "3   29.640      11-01  "
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[:3]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2021-04-09T07:39:58.841782Z",
     "iopub.status.busy": "2021-04-09T07:39:58.841030Z",
     "iopub.status.idle": "2021-04-09T07:39:58.867561Z",
     "shell.execute_reply": "2021-04-09T07:39:58.867164Z"
    },
    "papermill": {
     "duration": 0.056191,
     "end_time": "2021-04-09T07:39:58.867687",
     "exception": false,
     "start_time": "2021-04-09T07:39:58.811496",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>month_year</th>\n",
       "      <th>sales</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>11-01</td>\n",
       "      <td>98898.48886</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>11-02</td>\n",
       "      <td>91152.15698</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>11-03</td>\n",
       "      <td>145729.36736</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  month_year         sales\n",
       "0      11-01   98898.48886\n",
       "1      11-02   91152.15698\n",
       "2      11-03  145729.36736"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sales_per_month = data.groupby('month_year').sum()['sales'].reset_index()\n",
    "sales_per_month[:3]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2021-04-09T07:39:58.926678Z",
     "iopub.status.busy": "2021-04-09T07:39:58.925849Z",
     "iopub.status.idle": "2021-04-09T07:39:58.929528Z",
     "shell.execute_reply": "2021-04-09T07:39:58.929146Z"
    },
    "papermill": {
     "duration": 0.036382,
     "end_time": "2021-04-09T07:39:58.929658",
     "exception": false,
     "start_time": "2021-04-09T07:39:58.893276",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>month_year</th>\n",
       "      <th>sales</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>11-01</td>\n",
       "      <td>98898</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>11-02</td>\n",
       "      <td>91152</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>11-03</td>\n",
       "      <td>145729</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  month_year   sales\n",
       "0      11-01   98898\n",
       "1      11-02   91152\n",
       "2      11-03  145729"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sales_per_month['sales'] = sales_per_month['sales'].astype(int)\n",
    "sales_per_month[:3]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2021-04-09T07:39:59.001043Z",
     "iopub.status.busy": "2021-04-09T07:39:59.000198Z",
     "iopub.status.idle": "2021-04-09T07:39:59.402769Z",
     "shell.execute_reply": "2021-04-09T07:39:59.403167Z"
    },
    "papermill": {
     "duration": 0.447303,
     "end_time": "2021-04-09T07:39:59.403307",
     "exception": false,
     "start_time": "2021-04-09T07:39:58.956004",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1080x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(15,5))\n",
    "plt.plot(sales_per_month['month_year'], sales_per_month['sales'])\n",
    "plt.xticks(rotation='vertical', )\n",
    "plt.xlabel('Months of the year')\n",
    "plt.ylabel('Amount')\n",
    "plt.title('Sales/Month over 4 years span')\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "papermill": {
     "duration": 0.027795,
     "end_time": "2021-04-09T07:39:59.459539",
     "exception": false,
     "start_time": "2021-04-09T07:39:59.431744",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "## What's the most preferred shipment method?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2021-04-09T07:39:59.545681Z",
     "iopub.status.busy": "2021-04-09T07:39:59.544943Z",
     "iopub.status.idle": "2021-04-09T07:39:59.698652Z",
     "shell.execute_reply": "2021-04-09T07:39:59.699073Z"
    },
    "papermill": {
     "duration": 0.212157,
     "end_time": "2021-04-09T07:39:59.699208",
     "exception": false,
     "start_time": "2021-04-09T07:39:59.487051",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/opt/conda/lib/python3.7/site-packages/seaborn/_decorators.py:43: FutureWarning: Pass the following variable as a keyword arg: x. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.\n",
      "  FutureWarning\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 720x720 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(10,10))\n",
    "sns.countplot(data['ship_mode'])\n",
    "plt.xlabel('Shipment mode')\n",
    "plt.ylabel('Frequency')\n",
    "plt.title('Frequency of shipment mode')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "papermill": {
     "duration": 0.028562,
     "end_time": "2021-04-09T07:39:59.757483",
     "exception": false,
     "start_time": "2021-04-09T07:39:59.728921",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "## What are the most profitable category?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2021-04-09T07:39:59.820042Z",
     "iopub.status.busy": "2021-04-09T07:39:59.819363Z",
     "iopub.status.idle": "2021-04-09T07:39:59.841160Z",
     "shell.execute_reply": "2021-04-09T07:39:59.840725Z"
    },
    "papermill": {
     "duration": 0.055224,
     "end_time": "2021-04-09T07:39:59.841268",
     "exception": false,
     "start_time": "2021-04-09T07:39:59.786044",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "profit_per_category = pd.DataFrame(data.groupby(['category', 'sub_category']).sum()['profit'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2021-04-09T07:39:59.919155Z",
     "iopub.status.busy": "2021-04-09T07:39:59.918057Z",
     "iopub.status.idle": "2021-04-09T07:39:59.922225Z",
     "shell.execute_reply": "2021-04-09T07:39:59.922784Z"
    },
    "papermill": {
     "duration": 0.052781,
     "end_time": "2021-04-09T07:39:59.922953",
     "exception": false,
     "start_time": "2021-04-09T07:39:59.870172",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th>profit</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>category</th>\n",
       "      <th>sub_category</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th rowspan=\"4\" valign=\"top\">Technology</th>\n",
       "      <th>Copiers</th>\n",
       "      <td>258567.54818</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Phones</th>\n",
       "      <td>216717.00580</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Accessories</th>\n",
       "      <td>129626.30620</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Machines</th>\n",
       "      <td>58867.87300</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th rowspan=\"9\" valign=\"top\">Office Supplies</th>\n",
       "      <th>Appliances</th>\n",
       "      <td>141680.58940</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Storage</th>\n",
       "      <td>108461.48980</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Binders</th>\n",
       "      <td>72449.84600</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Paper</th>\n",
       "      <td>59207.68270</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Art</th>\n",
       "      <td>57953.91090</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Envelopes</th>\n",
       "      <td>29601.11630</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Supplies</th>\n",
       "      <td>22583.26310</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Labels</th>\n",
       "      <td>15010.51200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Fasteners</th>\n",
       "      <td>11525.42410</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th rowspan=\"4\" valign=\"top\">Furniture</th>\n",
       "      <th>Bookcases</th>\n",
       "      <td>161924.41950</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Chairs</th>\n",
       "      <td>141973.79750</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Furnishings</th>\n",
       "      <td>46967.42550</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Tables</th>\n",
       "      <td>-64083.38870</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                    profit\n",
       "category        sub_category              \n",
       "Technology      Copiers       258567.54818\n",
       "                Phones        216717.00580\n",
       "                Accessories   129626.30620\n",
       "                Machines       58867.87300\n",
       "Office Supplies Appliances    141680.58940\n",
       "                Storage       108461.48980\n",
       "                Binders        72449.84600\n",
       "                Paper          59207.68270\n",
       "                Art            57953.91090\n",
       "                Envelopes      29601.11630\n",
       "                Supplies       22583.26310\n",
       "                Labels         15010.51200\n",
       "                Fasteners      11525.42410\n",
       "Furniture       Bookcases     161924.41950\n",
       "                Chairs        141973.79750\n",
       "                Furnishings    46967.42550\n",
       "                Tables        -64083.38870"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "profit_per_category.sort_values(['category', 'profit'], ascending=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2021-04-09T07:39:59.992348Z",
     "iopub.status.busy": "2021-04-09T07:39:59.991553Z",
     "iopub.status.idle": "2021-04-09T07:39:59.996055Z",
     "shell.execute_reply": "2021-04-09T07:39:59.996468Z"
    },
    "papermill": {
     "duration": 0.041353,
     "end_time": "2021-04-09T07:39:59.996605",
     "exception": false,
     "start_time": "2021-04-09T07:39:59.955252",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1469034.8212799998"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "profit_sum = data['profit'].sum()\n",
    "profit_sum"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2021-04-09T07:40:00.074438Z",
     "iopub.status.busy": "2021-04-09T07:40:00.073643Z",
     "iopub.status.idle": "2021-04-09T07:40:00.077008Z",
     "shell.execute_reply": "2021-04-09T07:40:00.076413Z"
    },
    "papermill": {
     "duration": 0.043886,
     "end_time": "2021-04-09T07:40:00.077140",
     "exception": false,
     "start_time": "2021-04-09T07:40:00.033254",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "profit_per_category['percentage'] = profit_per_category['profit'].apply(lambda x: x/profit_sum*100)\n",
    "profit_per_category['percentage'] = profit_per_category['percentage'].round(decimals=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2021-04-09T07:40:00.154289Z",
     "iopub.status.busy": "2021-04-09T07:40:00.153373Z",
     "iopub.status.idle": "2021-04-09T07:40:00.157699Z",
     "shell.execute_reply": "2021-04-09T07:40:00.157127Z"
    },
    "papermill": {
     "duration": 0.04644,
     "end_time": "2021-04-09T07:40:00.157838",
     "exception": false,
     "start_time": "2021-04-09T07:40:00.111398",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th>profit</th>\n",
       "      <th>percentage</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>category</th>\n",
       "      <th>sub_category</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th rowspan=\"4\" valign=\"top\">Furniture</th>\n",
       "      <th>Bookcases</th>\n",
       "      <td>161924.41950</td>\n",
       "      <td>11.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Chairs</th>\n",
       "      <td>141973.79750</td>\n",
       "      <td>9.7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Furnishings</th>\n",
       "      <td>46967.42550</td>\n",
       "      <td>3.2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Tables</th>\n",
       "      <td>-64083.38870</td>\n",
       "      <td>-4.4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th rowspan=\"9\" valign=\"top\">Office Supplies</th>\n",
       "      <th>Appliances</th>\n",
       "      <td>141680.58940</td>\n",
       "      <td>9.6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Art</th>\n",
       "      <td>57953.91090</td>\n",
       "      <td>3.9</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Binders</th>\n",
       "      <td>72449.84600</td>\n",
       "      <td>4.9</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Envelopes</th>\n",
       "      <td>29601.11630</td>\n",
       "      <td>2.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Fasteners</th>\n",
       "      <td>11525.42410</td>\n",
       "      <td>0.8</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Labels</th>\n",
       "      <td>15010.51200</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Paper</th>\n",
       "      <td>59207.68270</td>\n",
       "      <td>4.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Storage</th>\n",
       "      <td>108461.48980</td>\n",
       "      <td>7.4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Supplies</th>\n",
       "      <td>22583.26310</td>\n",
       "      <td>1.5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th rowspan=\"4\" valign=\"top\">Technology</th>\n",
       "      <th>Accessories</th>\n",
       "      <td>129626.30620</td>\n",
       "      <td>8.8</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Copiers</th>\n",
       "      <td>258567.54818</td>\n",
       "      <td>17.6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Machines</th>\n",
       "      <td>58867.87300</td>\n",
       "      <td>4.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Phones</th>\n",
       "      <td>216717.00580</td>\n",
       "      <td>14.8</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                    profit  percentage\n",
       "category        sub_category                          \n",
       "Furniture       Bookcases     161924.41950        11.0\n",
       "                Chairs        141973.79750         9.7\n",
       "                Furnishings    46967.42550         3.2\n",
       "                Tables        -64083.38870        -4.4\n",
       "Office Supplies Appliances    141680.58940         9.6\n",
       "                Art            57953.91090         3.9\n",
       "                Binders        72449.84600         4.9\n",
       "                Envelopes      29601.11630         2.0\n",
       "                Fasteners      11525.42410         0.8\n",
       "                Labels         15010.51200         1.0\n",
       "                Paper          59207.68270         4.0\n",
       "                Storage       108461.48980         7.4\n",
       "                Supplies       22583.26310         1.5\n",
       "Technology      Accessories   129626.30620         8.8\n",
       "                Copiers       258567.54818        17.6\n",
       "                Machines       58867.87300         4.0\n",
       "                Phones        216717.00580        14.8"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "profit_per_category"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2021-04-09T07:40:00.236768Z",
     "iopub.status.busy": "2021-04-09T07:40:00.235839Z",
     "iopub.status.idle": "2021-04-09T07:40:00.239891Z",
     "shell.execute_reply": "2021-04-09T07:40:00.239434Z"
    },
    "papermill": {
     "duration": 0.047494,
     "end_time": "2021-04-09T07:40:00.240007",
     "exception": false,
     "start_time": "2021-04-09T07:40:00.192513",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th>profit</th>\n",
       "      <th>percentage</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>category</th>\n",
       "      <th>sub_category</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th rowspan=\"2\" valign=\"top\">Technology</th>\n",
       "      <th>Copiers</th>\n",
       "      <td>258567.54818</td>\n",
       "      <td>17.6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Phones</th>\n",
       "      <td>216717.00580</td>\n",
       "      <td>14.8</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th rowspan=\"2\" valign=\"top\">Furniture</th>\n",
       "      <th>Bookcases</th>\n",
       "      <td>161924.41950</td>\n",
       "      <td>11.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Chairs</th>\n",
       "      <td>141973.79750</td>\n",
       "      <td>9.7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Office Supplies</th>\n",
       "      <th>Appliances</th>\n",
       "      <td>141680.58940</td>\n",
       "      <td>9.6</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                    profit  percentage\n",
       "category        sub_category                          \n",
       "Technology      Copiers       258567.54818        17.6\n",
       "                Phones        216717.00580        14.8\n",
       "Furniture       Bookcases     161924.41950        11.0\n",
       "                Chairs        141973.79750         9.7\n",
       "Office Supplies Appliances    141680.58940         9.6"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "largest = profit_per_category.nlargest(5,'percentage')\n",
    "largest"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2021-04-09T07:40:00.307971Z",
     "iopub.status.busy": "2021-04-09T07:40:00.307380Z",
     "iopub.status.idle": "2021-04-09T07:40:00.311493Z",
     "shell.execute_reply": "2021-04-09T07:40:00.310915Z"
    },
    "papermill": {
     "duration": 0.038973,
     "end_time": "2021-04-09T07:40:00.311643",
     "exception": false,
     "start_time": "2021-04-09T07:40:00.272670",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Largest profitable products:\n",
      " [17.6, 14.8, 11.0, 9.7, 9.6]\n"
     ]
    }
   ],
   "source": [
    "print('Largest profitable products:\\n', largest['percentage'].tolist())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2021-04-09T07:40:00.379940Z",
     "iopub.status.busy": "2021-04-09T07:40:00.379240Z",
     "iopub.status.idle": "2021-04-09T07:40:00.381865Z",
     "shell.execute_reply": "2021-04-09T07:40:00.381458Z"
    },
    "papermill": {
     "duration": 0.03845,
     "end_time": "2021-04-09T07:40:00.381967",
     "exception": false,
     "start_time": "2021-04-09T07:40:00.343517",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "profit_per_category_reset = profit_per_category.reset_index()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2021-04-09T07:40:00.456110Z",
     "iopub.status.busy": "2021-04-09T07:40:00.455118Z",
     "iopub.status.idle": "2021-04-09T07:40:00.459314Z",
     "shell.execute_reply": "2021-04-09T07:40:00.458827Z"
    },
    "papermill": {
     "duration": 0.046702,
     "end_time": "2021-04-09T07:40:00.459681",
     "exception": false,
     "start_time": "2021-04-09T07:40:00.412979",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>category</th>\n",
       "      <th>profit</th>\n",
       "      <th>percentage</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Furniture</td>\n",
       "      <td>286782.25380</td>\n",
       "      <td>19.5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Office Supplies</td>\n",
       "      <td>518473.83430</td>\n",
       "      <td>35.1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Technology</td>\n",
       "      <td>663778.73318</td>\n",
       "      <td>45.2</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          category        profit  percentage\n",
       "0        Furniture  286782.25380        19.5\n",
       "1  Office Supplies  518473.83430        35.1\n",
       "2       Technology  663778.73318        45.2"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "profit_per_category_reset = profit_per_category_reset.groupby('category').sum()[['profit', 'percentage']]\n",
    "ppc = profit_per_category_reset.reset_index()\n",
    "ppc"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {
    "execution": {
     "iopub.execute_input": "2021-04-09T07:40:00.630929Z",
     "iopub.status.busy": "2021-04-09T07:40:00.630021Z",
     "iopub.status.idle": "2021-04-09T07:40:00.762039Z",
     "shell.execute_reply": "2021-04-09T07:40:00.762449Z"
    },
    "papermill": {
     "duration": 0.269941,
     "end_time": "2021-04-09T07:40:00.762609",
     "exception": false,
     "start_time": "2021-04-09T07:40:00.492668",
     "status": "completed"
    },
    "scrolled": true,
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "image/png": "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oz0Ro0i8UFIiItIxC7gTM6xTBKyn9b4qR3cxy1qOGbL6eptVOyL9noZvREREJCqop0RERESigpISERERiQpKSkRERCQqKCkRERGRqKCkRERERKKCkhIRERGJCkpKREREJCqoSrCIiHTZqlWrhiUkJNwPzEK/2MaKALDG5/NdM2/evANOB9MRJSUiItJlCQkJ948YMWL60KFDq1wul3bfjAGBQMAqKyubsW/fvvsxlamjlrJcERE5GrOGDh3qVUISO1wulz106NBqTO9WVFNSIiIiR8OlhCT2BP/Oov4zP+oDFBERCed2u+dNmzZtRuhRUlKS2BPXzcvLmwZQUlKSeO+992b1xDXl6GhOiYiIHLPs/MJ5PXm90ruWrOrsnKSkpMCGDRvWHe21W1pa8Hg87R4vKiraALBp06akRx99NOv666+vPJrr+3w+EhL0sdod6ikREZGYN3r06Ny9e/cmALzxxhupCxYsyAG49dZbR11++eXjTzzxxCmf+tSnJtx6662jLrvssuwFCxbkjBkzJvfHP/7xsNA1UlNT8wC++93vjl65cmXatGnTZtx5553D7r777sFf+MIXxoXOO+200yY/++yz6aHXfP3rXx81e/bsaS+//HLaH//4x6zc3Nzp06ZNm3HFFVeM9/l8ffuNiHFKSkREJKY0NTW5QkM3Z5111qTOzv/4449TX3jhhc3PPPPMNoDNmzcnv/766xs/+OCD9b/61a9GNTU1WeHn/+QnP9k9f/782g0bNqz7wQ9+0OES2oaGBtesWbMaPv744w1Dhw71/ec//8lauXLlhg0bNqxzuVz2vffeO7h777Z/UT+TiIjElKMdvjn33HMPpqWlHZqce/bZZx9MSUmxU1JSfFlZWS27du1KmDRpUsuxxOJ2u7nqqquqAJ5//vn0NWvWpM6ZM2c6QGNjo2vYsGHqKjkKSkpERCTmud1uOxAIAKb3IvzYgAEDAuFfJyUl2WGvw+fzteopaSshIeHQtcH01IT+nJiYGAjNI7Ft27rssssq/vCHP+zuxlvp1zR8IyIiMW/MmDHNb731VirAY489Nqg718rMzPTX1ta6Q19PmjSpee3atal+v5/Nmzd7Pv744wGRXnfuued6n3322UG7d+9OANi/f79748aNPbIyqL9QUiIiIjHvjjvu2HP77bePmzdvXo7b7e7WPioLFixoSEhIsHNycmbceeedw84666zasWPHNuXk5My8+eabx86YMaM+0uvmzZvX+L3vfW/3GWecMXXq1KkzTj/99Kk7d+5sf7mPHMGybe2BIyIiXbN69erSOXPmlDsdhxy91atXD5kzZ06203F0RD0lIiIiEhWUlIiIiEhUUFIiIiIiUUFJiYiIiEQFJSUiIiISFZSUiIiISFRQUiIiIjFly5YtnjPOOGPS+PHjZ40dO3bW1VdfPbaxsfHQrqwXXHDBhKlTp8648847hxUVFSVPmzZtxvTp02esXbs2KS8vb1p3779z586E0047bXJOTs6MSZMmzTzllFMmd/eabT377LPpp5122mSAhx9+OPM73/nOiJ6+RzTSNvMiInLsCjLn9ez1qld1dDgQCHDRRRdNvuaaaw7cfPPNW3w+H1dcccX4m2++efSf//znXTt27EhYtWpV2p49e4oBvvOd74w477zzDv7mN7/ZA1BUVLShuyF+61vfGn366ad7v//97x8AeO+991K6e82OfO5zn6sGqnvzHtFCPSUiIhIznnnmmfSkpKTAzTffXAGQkJDAvffeu/PRRx8dUlNT4zrzzDOnVlZWeqZNmzbjG9/4xsj77rtv+MMPPzxk4cKFUwFSU1PzQtf63ve+N3zq1KkzcnJyZtx4442jAdauXZv0iU98YsrMmTOnz5s3L6eoqCi5bQz79u3zjB07tjn09cKFCxugde8GwBe+8IVxd99992CA0aNH595www2jc3Nzp+fm5k5fs2ZNEsAll1ySfcUVV4ybN29eTnZ29qx//etfmW3vd/fddw/+whe+MA5gz549Ceecc86kWbNmTZ81a9b0F198cQBAYWFhWqhy8vTp02dUVVXF5Oe7ekpERCRmFBcXp8yZM6fVNu9ZWVmBkSNHNq9bty7pmWee2Xz++edPCVURtm3bSktL8//whz/cH/6axx57LKOwsHDQqlWrNqSnpwf279/vBrjmmmvG33fffdtzc3ObXnnllQE33HDDuHfffXdj+Gu/8pWvHLjqqqsm/ulPf6o/9dRTvTfccENFdnZ2p1WGMzIy/MXFxevvueeewV/96lfHvvrqq5sBdu7cmfT++++XrFu3LunMM8/MufDCC4vbu8aXv/zlsbfeeuv+c845p3bTpk2J55xzzpStW7eu/fWvfz3i7rvv3n722WfXVVdXu1JTUwPtXSOaKSkREZGYYds2lmUdUR8l2N7l67z00ksZn//858vT09MDAMOHD/dXV1e7ioqK0i677LJJofOam5uPuOgll1ziPemkk4qffPLJzOeffz5z3rx5M4qLi9d2ds9ly5ZVAlx77bWV3/ve98aGXa/S7XaTm5vbNHbs2KaPPvroiN6ZkLfeeitj06ZNh4aLamtr3VVVVa5FixbV3nbbbWM//elPV15++eVVkyZNUlIiIiLSm3JzcxuefvrpVlWAKysrXfv27UucPn160549e7r0uRYpifH7/aSnp/tCvSwdGT58uP/666+vvP766ytPO+20yS+++GLayJEjfYHA4Vygqamp1Q1crsMjKuGJVds4OkqubNtm5cqV69PS0lolZj/96U/3XXTRRdVPP/105uLFi6c///zzG/Py8ho7ex/RJibHnEREpH9aunRpTWNjo+uee+4ZDODz+bjxxhvHXnbZZYd6Pbri3HPP9T700ENDampqXAD79+93Z2VlBcaMGdP8wAMPDAIzqfadd945YhLrihUr0kOvq6qqcm3fvj1pwoQJzZMmTWravHlzSkNDg1VRUeF+8803M8Jf9/e//z0L4K9//eugvLy8ulD7E088Mcjv97N27dqknTt3Js2ZM6fdZOKkk07y/vznPx8W+vrtt99OATMXZsGCBQ0/+clP9uXm5tatWbOm3d6WaKaeEhERiRkul4unnnpq83XXXTf+l7/85chAIMDpp59efffdd+8+mutceuml3g8//DD1uOOOm+7xeOwzzzyz+p577tn9r3/9a+u11147/uc///lIn89nXXzxxZUnnHBCQ/hrP/jgg9RbbrllnNvttm3btq688sryU045pR7gggsuqJo+ffrMCRMmNM6cObPV3JempiZr9uzZ0wKBgPXII49sDbVPnjy5acGCBTkVFRWe3/72t9tTU1OPGJ4Kue+++3Zec80146ZOnTrD7/dbCxcurFm8ePGOX/ziF8PefvvtDJfLZU+dOrXh0ksvjcnVOpZtt/veRUREWlm9enXpnDlzyp2OI9aMHj06d+XKletHjhzpC2+/5JJLss8///zqq6++uqq3Y1i9evWQOXPmZPf2fbpDwzciIiISFTR8IyIi0st2794dcZnv448/XtrHoUQ19ZSIiIhIVFBSIiIiIlFBwzcicmwKMi0gExgMZLV5RGoLLa20uvBsAw1A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\n",
      "text/plain": [
       "<Figure size 792x576 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(11,8))\n",
    "\n",
    "plt.pie(ppc['percentage'], \n",
    "        labels=ppc['category'], \n",
    "        shadow=True,\n",
    "        explode=(0,.05,.05),\n",
    "        textprops=dict(color='w', fontsize=20),\n",
    "        autopct='%1.0f%%')\n",
    "\n",
    "plt.title('Profits Per Category')\n",
    "plt.legend(loc='upper right') \n",
    "plt.show() "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.9"
  },
  "papermill": {
   "default_parameters": {},
   "duration": 43.775206,
   "end_time": "2021-04-09T07:40:02.490862",
   "environment_variables": {},
   "exception": null,
   "input_path": "__notebook__.ipynb",
   "output_path": "__notebook__.ipynb",
   "parameters": {},
   "start_time": "2021-04-09T07:39:18.715656",
   "version": "2.2.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
