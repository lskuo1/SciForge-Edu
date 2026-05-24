from src.workspace.draft import WorkspaceDraft


def test_create_workspace():

    w = WorkspaceDraft(

        draft_id="draft001",

        title="Grade8 Midterm"
    )

    assert w.draft_id == "draft001"

    assert w.selected_questions == []


def test_default_values():

    w = WorkspaceDraft(

        draft_id="draft002",

        title="Physics"
    )

    assert w.settings == {}