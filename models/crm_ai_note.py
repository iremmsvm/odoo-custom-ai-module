from odoo import models, fields


class CrmAiNote(models.Model):
    _name = "crm.ai.note"
    _description = "CRM AI Note Analysis"

    name = fields.Char(string="Note Title", required=True)
    note_text = fields.Text(string="Customer Note")
    summary = fields.Text(string="AI Summary", readonly=True)
    sentiment = fields.Selection(
        [
            ("positive", "Positive"),
            ("neutral", "Neutral"),
            ("negative", "Negative"),
        ],
        string="Sentiment",
        readonly=True,
    )

    def action_analyze_note(self):
        for record in self:
            text = record.note_text or ""

            # Mock AI logic
            record.summary = text[:120] + "..." if len(text) > 120 else text

            if "problem" in text.lower():
                record.sentiment = "negative"
            elif "good" in text.lower():
                record.sentiment = "positive"
            else:
                record.sentiment = "neutral"
