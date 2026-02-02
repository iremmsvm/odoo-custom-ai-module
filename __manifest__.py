{
    "name": "CRM AI Note Analyzer",
    "version": "1.0",
    "summary": "AI-powered analysis for CRM customer notes",
    "description": """
Adds AI-based text analysis features to CRM customer notes
to support smarter business decisions.
    """,
    "category": "CRM",
    "author": "Irem Sevim",
    "depends": ["crm"],
    "data": [
        "security/ir.model.access.csv",
        "views/crm_ai_note_view.xml",
    ],
    "installable": True,
    "application": False,
}
