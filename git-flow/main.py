from manim import *

class GitFlowVisualization(Scene):
    def construct(self):
        # タイトル
        title = Text("Git Flow Visualization", font_size=36).shift(UP * 3.2)
        self.play(Write(title))
        self.wait(1)
        
        # ブランチを表現する線（画面内に収まるように短縮）
        main_branch = Line(LEFT * 4, RIGHT * 4, color=BLUE).shift(UP * 1.5)
        feature_branch = Line(LEFT * 1, RIGHT * 3, color=GREEN).shift(DOWN * 0.5)
        
        # ブランチラベル
        main_label = Text("main", font_size=20, color=BLUE).next_to(main_branch, LEFT, buff=0.3)
        feature_label = Text("feature", font_size=20, color=GREEN).next_to(feature_branch, LEFT, buff=0.3)
        
        self.play(Create(main_branch), Write(main_label))
        self.wait(0.5)
        
        # Step 1: Checkout (新しいブランチの作成)
        step1_text = Text("1. Checkout (新しいブランチ作成)", font_size=24, color=YELLOW).shift(DOWN * 3.2)
        self.play(Write(step1_text))
        
        # フィーチャーブランチの分岐を表示
        branch_point = Dot(main_branch.get_start() + RIGHT * 1.5, color=WHITE)
        branch_line = Line(branch_point.get_center(), feature_branch.get_start(), color=GREEN)
        
        self.play(Create(branch_point))
        self.play(Create(branch_line), Create(feature_branch), Write(feature_label))
        self.wait(2)
        
        # Step 2: Add (変更をステージング)
        self.play(Transform(step1_text, Text("2. Add (変更をステージング)", font_size=24, color=YELLOW).shift(DOWN * 3.2)))
        
        # ワーキングディレクトリとステージング領域（位置を調整）
        working_dir = Rectangle(width=1.5, height=1, color=RED).shift(LEFT * 3 + DOWN * 2)
        staging_area = Rectangle(width=1.5, height=1, color=ORANGE).shift(LEFT * 0.5 + DOWN * 2)
        
        working_label = Text("Working\nDirectory", font_size=16).move_to(working_dir)
        staging_label = Text("Staging\nArea", font_size=16).move_to(staging_area)
        
        # ファイルを表現する小さな矩形
        file1 = Rectangle(width=0.3, height=0.3, color=WHITE).move_to(working_dir.get_center() + UP * 0.3)
        file2 = Rectangle(width=0.3, height=0.3, color=WHITE).move_to(working_dir.get_center() + DOWN * 0.3)
        
        self.play(Create(working_dir), Create(staging_area))
        self.play(Write(working_label), Write(staging_label))
        self.play(Create(file1), Create(file2))
        
        # ファイルをステージング領域に移動
        file1_copy = file1.copy().move_to(staging_area.get_center() + UP * 0.3)
        file2_copy = file2.copy().move_to(staging_area.get_center() + DOWN * 0.3)
        
        self.play(Transform(file1, file1_copy), Transform(file2, file2_copy))
        self.wait(2)
        
        # Step 3: Commit (変更をコミット)
        self.play(Transform(step1_text, Text("3. Commit (変更をコミット)", font_size=24, color=YELLOW).shift(DOWN * 3.2)))
        
        # コミットを表現する円
        commit1 = Circle(radius=0.15, color=GREEN, fill_opacity=1).move_to(feature_branch.get_start() + RIGHT * 0.8)
        commit2 = Circle(radius=0.15, color=GREEN, fill_opacity=1).move_to(feature_branch.get_start() + RIGHT * 2)
        
        self.play(Create(commit1))
        self.wait(0.5)
        self.play(Create(commit2))
        
        # ファイルがコミットに含まれることを示す
        self.play(FadeOut(file1), FadeOut(file2), FadeOut(working_dir), FadeOut(staging_area), 
                 FadeOut(working_label), FadeOut(staging_label))
        self.wait(2)
        
        # Step 4: Push (リモートリポジトリへプッシュ)
        self.play(Transform(step1_text, Text("4. Push (リモートリポジトリへ)", font_size=24, color=YELLOW).shift(DOWN * 3.2)))
        
        # リモートリポジトリを表現
        remote_branch = Line(LEFT * 1, RIGHT * 3, color=GREEN, stroke_width=6).shift(DOWN * 1.8)
        remote_label = Text("remote/feature", font_size=16, color=GREEN).next_to(remote_branch, LEFT, buff=0.3)
        
        # プッシュのアニメーション（矢印）
        push_arrow = Arrow(feature_branch.get_center(), remote_branch.get_center(), color=YELLOW, stroke_width=4)
        
        self.play(Create(push_arrow))
        self.play(Create(remote_branch), Write(remote_label))
        self.play(FadeOut(push_arrow))
        self.wait(2)
        
        # Step 5: Merge (メインブランチにマージ)
        self.play(Transform(step1_text, Text("5. Merge (メインブランチにマージ)", font_size=24, color=YELLOW).shift(DOWN * 3.2)))
        
        # マージポイント
        merge_point = Dot(main_branch.get_end() + LEFT * 0.5, color=PURPLE, radius=0.2)
        merge_line = Line(feature_branch.get_end(), merge_point.get_center(), color=PURPLE, stroke_width=3)
        
        # マージアニメーション
        self.play(Create(merge_line))
        self.play(Create(merge_point))
        
        # 完了メッセージ
        completion_text = Text("Git Flow Complete!", font_size=30, color=GREEN).shift(UP * 2.8)
        self.play(Transform(step1_text, completion_text))
        self.wait(3)
        
        # 全体をフェードアウト
        self.play(FadeOut(Group(*self.mobjects)))
