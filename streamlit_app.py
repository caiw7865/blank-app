import streamlit as st
import json

# -------------------------- 页面配置 --------------------------
st.set_page_config(
    page_title="RDF + JSON 查看器",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -------------------------- 自定义CSS --------------------------
st.markdown("""
<style>
/* 代码块样式 */
.code-block {
    background-color: #f8f9fa;
    padding: 20px;
    border-radius: 8px;
    border: 1px solid #e9ecef;
    font-family: monospace;
    white-space: pre;
    overflow-x: auto;
    height: 550px;
}
/* 底部间距 */
.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
}
</style>
""", unsafe_allow_html=True)

# ==================== 核心数据 ====================
turtle_code = """okgm:AsdKB  a  okgm:Okg;
    dcat:distribution okgm:AsdKB_instance .
okgm:AsdKB_instance  a  okgm:Distribution;
    dct:title "AsdKB的实例三元组文件";
    dcat:downloadURL <https://zenodo.org/records/8199698/files/instance.zip?download=1>;
    dcat:accessURL <https://zenodo.org/records/8199698/preview/instance.zip?include_deleted=0>;
    dcat:byteSize "3145728"^^xsd:long;      
    dcat:format "zip";
    dct:license odrl:CC_BY_4.0;
    dct:creator foaf:SoutheastUniversity ;
    okgm:hasService  okgm:ASD_Web;
    okgm:checksum  okgm:ASD_checksum.
odrl:CC_BY_4.0  a  odrl:Policy;  
    dct:title "CC BY 4.0";
    rdfs:label "Open Data Commons Attribution License";
    owl:sameAs <https://creativecommons.org/licenses/by/4.0/legalcode> .
foaf:SoutheastUniversity  a  foaf:Agent;
    foaf:name "东南大学" ;
    foaf:mbox <http://data.openkg.cn/organization/seu>.
okgm:ASD_Web  a  okgm:Service;
    dct:title "ASD知识可视化";
    okgm:serviceType   "Web可视化服务门户";
    sd:endpoint  <http://asdkb.org.cn/AsdKB>.
okgm:ASD_checksum  a  okgm:checksum;
    spdx:algorithm  "Message-Digest Algorithm 5";
    spdx:chechsumValue  "7792a996285d3ac284450f006ac5c37d".
"""

# 对应的JSON结构
json_data = {
    "okgm:AsdKB": {
        "a": "okgm:Okg",
        "dcat:distribution": "okgm:AsdKB_instance"
    },
    "okgm:AsdKB_instance": {
        "a": "okgm:Distribution",
        "dct:title": "AsdKB的实例三元组文件",
        "dcat:downloadURL": "https://zenodo.org/records/8199698/files/instance.zip?download=1",
        "dcat:accessURL": "https://zenodo.org/records/8199698/preview/instance.zip?include_deleted=0",
        "dcat:byteSize": "3145728",
        "dcat:format": "zip",
        "dct:license": "odrl:CC_BY_4.0",
        "dct:creator": "foaf:SoutheastUniversity",
        "okgm:hasService": "okgm:ASD_Web",
        "okgm:checksum": "okgm:ASD_checksum"
    },
    "odrl:CC_BY_4.0": {
        "a": "odrl:Policy",
        "dct:title": "CC BY 4.0",
        "rdfs:label": "Open Data Commons Attribution License",
        "owl:sameAs": "https://creativecommons.org/licenses/by/4.0/legalcode"
    },
    "foaf:SoutheastUniversity": {
        "a": "foaf:Agent",
        "foaf:name": "东南大学",
        "foaf:mbox": "http://data.openkg.cn/organization/seu"
    },
    "okgm:ASD_Web": {
        "a": "okgm:Service",
        "dct:title": "ASD知识可视化",
        "okgm:serviceType": "Web可视化服务门户",
        "sd:endpoint": "http://asdkb.org.cn/AsdKB"
    },
    "okgm:ASD_checksum": {
        "a": "okgm:checksum",
        "spdx:algorithm": "Message-Digest Algorithm 5",
        "spdx:chechsumValue": "7792a996285d3ac284450f006ac5c37d"
    }
}

json_str = json.dumps(json_data, ensure_ascii=False, indent=4)

# -------------------------- 页面布局 --------------------------
st.title("RDF 三元组（Turtle）与 JSON 对照查看")
st.divider()

# 左右分栏
left_col, right_col = st.columns([1, 1], gap="large")

# ========== 左侧：Turtle RDF 三元组 ==========
with left_col:
    st.subheader("📄 Turtle 格式（RDF 三元组）")
    st.markdown(f"<div class='code-block'>{turtle_code}</div>", unsafe_allow_html=True)

# ========== 右侧：JSON + 下载按钮 ==========
with right_col:
    st.subheader("📄 JSON 格式")
    st.markdown(f"<div class='code-block'>{json_str}</div>", unsafe_allow_html=True)
    
    st.divider()
    
    # 下载按钮
    st.download_button(
        label="⬇ 下载 JSON 文件",
        data=json_str,
        file_name="asdkb_metadata.json",
        mime="application/json",
        use_container_width=True,
        type="primary"
    )
